import os
from flask import Flask
from api.main import api
from site_frontend.site import web
from config import Config


app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(web)


# b_token = app.config['BOT_TOKEN']
# u_token = app.config['USER_TOKEN']
# veri = app.config['VERIFICATION_TOKEN']
# oauth_scope = app.config['OAUTH_SCOPE']
# client_id = app.config['CLIENT_ID']
# client_secret = app.config['CLIENT_SECRET']
#
