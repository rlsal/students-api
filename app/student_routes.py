import json

from flask import jsonify, request, make_response

from app import app, db
from app.models import Student, Course


@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    response = [{'first_name': s.first_name, 'last_name': s.last_name, 'email': s.email} for s in students]
    return make_response(json.dumps(response), 200)


@app.route('/students', methods=['POST'])
def add_student():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')

    if not (first_name or last_name or email):
        make_response("Missing relevant params", 400)

    student = Student(first_name, last_name, email)

    db.session.add(student)
    db.session.commit()

    return student_response(student)


@app.route('/students/<string:email>', methods=['GET'])
def get_student(email):
    student = Student.query.filter(Student.email == email).first()

    if not student:
        make_response("No student found", 404)

    return student_response(student)


@app.route('/student/<string:email>', methods=['PATCH'])
def update_student(email):
    student = Student.query.filter(Student.email == email).first()
    first_name = request.json['first_name'] if request.json.get('first_name') else None
    last_name = request.json['last_name'] if request.json.get('last_name') else None

    if not student:
        return make_response("No student found", 404)

    if not first_name and last_name:
        return make_response("Missing relevant params", 400)

    student.first_name = first_name if first_name else student.first_name
    student.last_name = last_name if last_name else student.last_name
    db.session.commit()

    return student_response(student)


@app.route('/student/<string:email>', methods=['DELETE'])
def delete_student(email):
    student = Student.query.filter(Student.email == email).first()

    if not student:
        return make_response("No such email: " + email, 404)

    db.session.delete(student)
    db.session.commit()

    return student_response(student)


@app.route('/coursestudent/<int:course_id>/<int:student_id>/', methods=['POST'])
def add_student_to_course(course_id, student_id):
    course = Course.query.filter(Course.id == course_id).first()
    student = Student.query.filter(Student.id == student_id).first()
    course.listed_students.append(student)
    db.session.commit()

    return make_response(student.first_name + " " + student.last_name + " was added to Course " + course.name , 200)


@app.route('/coursestudent/<int:course_id>/<int:student_id>/', methods=['DELETE'])
def remvove_student_from_course(course_id, student_id):
    course = Course.query.filter(Course.id == course_id).first()
    student = Student.query.filter(Student.id == student_id).first()
    flag = False

    for student in course.listed_students:
        if student.id == student_id:
            course.listed_students.remove(student)
            flag = True

    if flag:
        db.session.commit()

        return make_response(student.first_name + " " + student.last_name + " was removed from Course"
                                                                            " " + course.name , 200)

    return make_response("Can't remove a student that isn't part of the course", 400)


def student_response(student):
    format_student = {'first_name': student.first_name,
                      'last_name': student.last_name,
                      'email': student.email}
    return make_response(jsonify(format_student), 200)

