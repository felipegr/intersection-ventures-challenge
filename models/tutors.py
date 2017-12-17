# -*- coding: utf-8 -*-

from app import db

from flask_sqlalchemy import orm
from sqlalchemy import (
    Column, DateTime, Integer, String, Text
)


class Tutors(db.Model):
    __tablename__ = 'tutors'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    document_no = Column(String(20), unique=True)


orm.configure_mappers()
