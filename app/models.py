from sqlalchemy import ForeignKey
from app import db

students_courses_association = db.Table('students_courses',
                                        db.Column('student_id', db.Integer, ForeignKey('students.id')),
                                        db.Column('course_id', db.Integer, ForeignKey('courses.id')))


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    courses = db.relationship('Course', secondary=students_courses_association, backref=db.backref('listed_students'))
    grades = db.relationship('Grade', backref='performance')

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class Grade(db.Model):
    __tablename__ = 'grades'

    grade = db.Column(db.Integer(), nullable=False)
    performance_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    def __init__(self, grade, performance_id, course_id):
        self.grade = grade
        self.performance_id = performance_id
        self.course_id = course_id
