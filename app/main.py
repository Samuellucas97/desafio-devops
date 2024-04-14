from flask import Flask, jsonify, request, session, redirect, url_for
from functools import wraps
from requests import get

from authlib.integrations.flask_client import OAuth
from http import HTTPStatus
from flask_wtf.csrf import CSRFProtect, generate_csrf



from config import KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET, KEYCLOAK_AUTHORIZATION_URL
from config import KEYCLOAK_TOKEN_URL, KEYCLOAK_USERINFO_URL, KEYCLOAK_REDIRECT_URI
from config import FLASK_SECRET_KEY, KEYCLOAK_JWKS_URI, KEYCLOAK_LOGOUT_URL


# from api.utils import logger

app_name = 'comentarios'
app = Flask(app_name)
app.secret_key= FLASK_SECRET_KEY
app.debug = True

csrf = CSRFProtect(app)


comments: dict = {}


oauth = OAuth(app)
oauth.register(
    name='keycloak',
    client_id=KEYCLOAK_CLIENT_ID,
    client_secret=KEYCLOAK_CLIENT_SECRET,
    authorize_url=KEYCLOAK_AUTHORIZATION_URL,
    authorize_params={'scope': 'openid profile email', 'nonce': 'your-nonce-value'},
    access_token_url=KEYCLOAK_TOKEN_URL,
    userinfo_endpoint=KEYCLOAK_USERINFO_URL,
    jwks_uri=KEYCLOAK_JWKS_URI,
    client_kwargs={'scope':'openid profile email'}
)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_info' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@login_required
def index():
    app.logger.info('Calling index function')
    user_info = session.get('user_info')
    
    if user_info:
        return user_info
    

    

@app.route('/login')
def login():
    app.logger.info('Calling login function')
    csrf_token = generate_csrf()
    app.logger.debug('csrf_token: %s', csrf_token)
    session['csrf_token'] = csrf_token
    return oauth.keycloak.authorize_redirect(redirect_uri=KEYCLOAK_REDIRECT_URI, state=csrf_token)

@app.route('/logout')
def logout():
    app.logger.info('Calling logout function')
    session.pop('user_info', None)
    
    logout_response = get(KEYCLOAK_LOGOUT_URL)
    return redirect(logout_response.url)


@app.route('/callback')
def callback():
    app.logger.info('Calling callback function')
    csrf_token = session.pop('csrf_token', None)
    app.logger.debug('csrf_token: %s', csrf_token)

    state = request.args.get('state')
    app.logger.debug('state: %s', state)
    
    if csrf_token != state:
        return {'message': 'Invalid CSRF Token' }, HTTPStatus.FORBIDDEN
    
    token = oauth.keycloak.authorize_access_token()
    app.logger.debug('Access Token: %s', token)
    nonce = session.pop('nonce', None)
    user_info = oauth.keycloak.parse_id_token(token, nonce=nonce)
    app.logger.debug('User info: %s', user_info)
    
    session['user_info'] = user_info
    return redirect(url_for('index'))


@app.route('/api/comment/new', methods=['POST'])
@login_required
def api_comment_new():
    request_data = request.get_json()

    email = request_data['email']
    comment = request_data['comment']
    content_id = '{}'.format(request_data['content_id'])

    new_comment = {
            'email': email,
            'comment': comment,
        }

    if content_id in comments:
        comments[content_id].append(new_comment)
    else:
        comments[content_id] = [new_comment]

    message = 'comment created and associated with content_id {}'.format(content_id)
    response = {
            'status': HTTPStatus.OK,
            'message': message,
            }
    return jsonify(response), HTTPStatus.OK


@app.route('/api/comment/list/<content_id>')
@login_required
def api_comment_list(content_id):
    content_id = '{}'.format(content_id)
    app.logger.info('Trying to retrieve comment')
    

    if content_id in comments:
        return jsonify(comments[content_id])
    else:
        app.logger.error('Comment id %s does not exist', content_id)
        message = 'content_id {} not found'.format(content_id)
        response = {
                'status': HTTPStatus.NOT_FOUND,
                'message': message,
                }
        return jsonify(response), HTTPStatus.NOT_FOUND


@app.route('/health')
def api_healthcheck():
    return {}, HTTPStatus.OK
