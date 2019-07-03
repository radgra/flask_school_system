from db import db


class Grade(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True)
    learning_class_student_id = db.Column(db.Integer, db.ForeignKey("learning_class_students.id"))
    grade = db.Column(db.Integer)

    lecture_student = db.relationship("LectureStudents", back_populates="grades")
