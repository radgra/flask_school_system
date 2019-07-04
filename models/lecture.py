from db import db


class Lecture(db.Model):
    __tablename__ = 'lectures'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(255), nullable=False) #czy nullable false is by default ?
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)

    teacher = db.relationship('Teacher', back_populates="lectures")
    students = db.relationship('LectureStudents', back_populates="lecture")


