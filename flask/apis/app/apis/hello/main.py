import site
site.addsitedir('utils')
site.addsitedir('controllers')

from helpers import hi_world
from http_controller import HttpController as http

from flask import Blueprint
hello_api = Blueprint('hello_api', __name__)

@hello_api.route('/')
@http.response_json
def hello():
    return hi_world()