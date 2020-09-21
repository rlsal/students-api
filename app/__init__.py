from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app


app = create_app()
db = SQLAlchemy(app)
api = Api(app)


from app import student_routes
from app import courses_route
from app import grades_route
