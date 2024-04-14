from os import urandom

FLASK_SECRET_KEY = urandom(24)

LOGSTASH_HOST='localhost'
LOGSTASH_PORT=5000 
LOGGING_FORMAT='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

KEYCLOAK_BASE_URL='http://localhost:8080'
KEYCLOAK_REALM='desafio-devops'
KEYCLOAK_CLIENT_ID='app'
KEYCLOAK_CLIENT_SECRET='iF0lbnfrexgY6Z2xvg4U4uT2ngteFVWO'
KEYCLOAK_REDIRECT_URI='http://localhost:8000/callback'
KEYCLOAK_AUTHORIZATION_URL=f'{KEYCLOAK_BASE_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/auth'
KEYCLOAK_TOKEN_URL=f'{KEYCLOAK_BASE_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token'
KEYCLOAK_USERINFO_URL=f'{KEYCLOAK_BASE_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/userinfo'
KEYCLOAK_JWKS_URI=f'{KEYCLOAK_BASE_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/certs'
KEYCLOAK_LOGOUT_URL=f'{KEYCLOAK_BASE_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/logout'