from flask import Flask
from authlib.flask.client import OAuth
from loginpass import create_flask_blueprint, Authlib

app = Flask(__name__)
app.secret_key = "secre1"
oauth = OAuth(app)


def handle_authorize(remote, token, user_info):
    if token:
        save_token(remote.name, token)
    if user_info:
        save_user(user_info)
        return user_page
    raise some_error

authlib_bp = create_flask_blueprint(Authlib, oauth, handle_authorize)
app.register_blueprint(authlib_bp, url_prefix='/authlib')
