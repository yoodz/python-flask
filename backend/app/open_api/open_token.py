from flask import request
from flask_restful import Resource, reqparse
from peewee import *
import logging
import time
import datetime
import os
import uuid

import traceback

from models import Project
from logger import *

logger = logging.getLogger("logger")

class token(Resource):
    def get(self):
        name = request.args.get('name')
        project = Project.select().where(Project.name == name).first()
        if project is None:
            return {"code": 500, "data": 'error name'}
        if datetime.datetime.strptime(project.expire_data, '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.fromtimestamp(time.time()):
            # 过期了，需要重新生成
            project.token = uuid.uuid1()
            project.expire_data = datetime.datetime.now() + datetime.timedelta(days=1)
            project.save()
        return {"code": 200, "token": str(project.token)}

    def post(self):
        data = request.get_json()
        name = data['name']
        floder_name = data['floder_name']

        project = Project.select().where(Project.name == name).first()
        if project:
            return {"code": 500, "data": 'exist error'}

        project = Project()
        project.token = uuid.uuid1()
        project.name = name
        project.expire_data = datetime.datetime.now() + datetime.timedelta(days=1)
        project.floder_name = floder_name
        project.save()
        return {"code": 200, "data": 'insert success'}