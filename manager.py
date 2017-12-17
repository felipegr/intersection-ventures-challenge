# -*- coding: utf-8 -*-

from app import create_app
import models

from flask_script import Manager


app = create_app()
manager = Manager(app)


@manager.command
def init_db():
    models.init_db()


if __name__ == '__main__':
    manager.run()
