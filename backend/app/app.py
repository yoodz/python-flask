#coding:utf8
import logging
import os

from flask import Flask, Response, render_template, request, redirect, session, g, jsonify, send_from_directory
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_restful import Api

from models import *
from open_api import open_file, open_token
from logger import *

logger = logging.getLogger("logger")
context = Flask(__name__)
context.config['SECRET_KEY'] = 'gnfsdascvxczaf'
api = Api(context)
CORS(context)


@context.before_request
def before_request():
    if request.path.startswith('/static'):
        return
    g.version = 2

    g.db = db
    if g.db.is_closed():
        g.db.connect()


@context.after_request
def after_request(response):
    if hasattr(g,'db'):
        if not g.db.is_closed():
            g.db.close()
    return response

api.add_resource(open_file.upload, '/openApi/upload')
api.add_resource(open_token.token, '/openApi/token')

def main():
    context.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()
