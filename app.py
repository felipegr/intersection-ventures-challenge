# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutors.sqlite3'
    app.config['SECRET_KEY'] = "ajshbdjahsbdjahsbd"
    
    db.init_app(app)
    
    from tutor_match.api import api
    from tutor_match.views import root
    app.register_blueprint(api)
    app.register_blueprint(root)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
