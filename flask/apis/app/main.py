# -*- coding:utf8 -*-
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

hello_api = __import__('apis.hello.main', fromlist=['hello_api']).hello_api
app.register_blueprint(hello_api, url_prefix='/hello_world')

if __name__ == "__main__":
    pass

