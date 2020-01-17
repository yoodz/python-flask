from flask import request
from flask_restful import Resource, reqparse
from peewee import *
import logging
import time
import os
import json

import traceback

from models import Project, Log
from logger import *
import const


logger = logging.getLogger("logger")

class upload(Resource):
    def post(self):
        token = request.headers.get('token') if request.headers.get("token") else ''
        logger.error("enter upload, token : %s" %(token))

        if token is '':
            return {"code": 200, "data": 'error token'}

        project = Project.select().where(Project.token == token, Project.expire_data > datetime.datetime.now()).first()
        if project is None:
            return {"code": 500, "data": 'please get token first'}

        log = Log()
        log.project = project.id
        log.save()
        return {"code": 200, "data": log.to_json()}
           
