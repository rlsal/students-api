from flask import make_response

from app import app, db
from app.models import Grade, Student, Course


@app.route('/grades/<int:student_id>/<int:course_id>/', methods=['GET'])
def get_student_grades(student_id, course_id):
    student_grade = Grade.query.filter(Grade.performance_id == student_id)\
        .filter(Grade.course_id == course_id).first()

    if not student_grade:
        return make_response("Not found", 404)

    return make_response(str(student_grade.grade), 200)


@app.route('/grades/<int:student_id>/<int:course_id>/<int:grade>', methods=['POST'])
def add_student_grade(student_id, course_id, grade):
    try:
        student = Student.query.filter(Student.id == student_id).first()
        course = Course.query.filter(Course.id == course_id).first()
        grade = Grade(grade, performance_id=student_id, course_id=course_id)
        db.session.add(grade)
        db.session.commit()

        return make_response(student.first_name + " " + student.last_name +"'s grade was added to course " + course.name)

    except Exception:
        return make_response("An error occured", 500)
