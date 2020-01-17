# -*- coding: utf-8 -*-
import datetime
from peewee import *
from playhouse.db_url import connect
from playhouse.shortcuts import model_to_dict, dict_to_model
from playhouse.migrate import MySQLMigrator, migrate
import const
import time
import json
from flask import current_app  # 导入当前的app应用


db = connect(const.MYSQL_CONFIG)


class BaseModel(Model):
    class Meta:
        database = db

    def to_json(self):
        return model_to_dict(self)

    def to_model(self, data):
        return dict_to_model(self, data)

class Log(BaseModel):
    id = AutoField(primary_key=True)
    project = CharField(default="")
    url = CharField(default="")
    descript = TextField(default="")
    deleted = IntegerField(default=0)
    created_time = CharField(default=datetime.datetime.now)

class Project(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(default="")
    token = TextField(default="")
    floder_name = TextField(default="")
    expire_data = CharField(default=datetime.datetime.now)
    created_time = CharField(default=datetime.datetime.now)
    deleted = IntegerField(default=0)

db.create_tables([Log, Project])
