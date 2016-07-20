#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'su_user'
    user_id = db.Column(db.String(30), primary_key=True, unique=True)
    user_name = db.Column(db.String(30))
    point = db.Column(db.Integer)
    created = db.Column(db.DateTime)

    def __init__(self, user_id, user_name, point):
        self.user_id = user_id
        self.user_name = user_name
        self.point = point
        self.created = datetime.now()

    def __repr__(self):
        return '{user_id : "%s", user_name : "%s", point : "%d"}' %\
               {self.user_id, self.user_name, self.point}