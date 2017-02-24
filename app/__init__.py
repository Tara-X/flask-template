# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_cors import CORS

from app.utils.web_util import common_error_handler, default_error_handler

from app.routes import general
from app.routes.auth import auth

app = Flask(__name__)


app.register_blueprint(general.mod)
app.register_blueprint(auth.mod)


app.register_error_handler(400, common_error_handler(400))
app.register_error_handler(403, common_error_handler(403))
app.register_error_handler(500, common_error_handler(500))
app.register_error_handler(Exception, default_error_handler)

CORS(app, supports_credentials=True)





