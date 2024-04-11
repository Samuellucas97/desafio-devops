from flask import Flask
from flask import jsonify
from flask import request

from http import HTTPStatus

from api.utils import logger

app_name = 'comentarios'
app = Flask(app_name)
app.debug = True

comments = {}


@app.route('/api/comment/new', methods=['POST'])
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