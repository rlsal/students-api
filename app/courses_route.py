import json

from flask import jsonify, request, make_response

from app import app, db
from app.models import Course


@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    response = [{'name': c.name} for c in courses]
    return make_response(json.dumps(response), 200)


@app.route('/courses', methods=['POST'])
def add_course():
    name = request.json.get('name')

    if not name:
        make_response("Missing relevant params", 400)

    course = Course(name)
    db.session.add(course)
    db.session.commit()

    return student_response(course)


@app.route('/courses/<string:name>', methods=['GET'])
def get_course(name):
    course = Course.query.filter(Course.name == name).first()

    if not course:
        make_response("No course found", 404)

    return student_response(course)


@app.route('/courses/<string:name>', methods=['PATCH'])
def update_course(name):
    course = Course.query.filter(Course.name == name).first()
    name = request.json['name'] if request.json.get('name') else None

    if not course:
        return make_response("No course found", 404)

    course.name = name
    db.session.commit()

    return student_response(course)


@app.route('/courses/<string:name>', methods=['DELETE'])
def delete_course(name):
    course = Course.query.filter(Course.name == name).first()

    if not course:
        return make_response("No course named " + name, 404)

    db.session.delete(course)
    db.session.commit()

    return student_response(course)


def student_response(course):
    format_course = {'name': course.name}
    return make_response(jsonify(format_course), 200)