# -*- coding:utf8 -*-
from main import app as application

if __name__ == "__main__":
    application.secret_key = 'test'
    application.run(threaded=True, host='0.0.0.0', port=80)
