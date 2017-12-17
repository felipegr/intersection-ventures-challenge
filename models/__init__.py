# -*- coding: utf-8 -*-

from app import db


def init_db():
    db.metadata.drop_all(bind=db.engine)
    db.metadata.create_all(bind=db.engine)
