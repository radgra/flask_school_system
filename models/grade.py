from db import db


class Grade(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True)
    lecture_student_id = db.Column(db.Integer, db.ForeignKey("lecture_students.id"))
    grade = db.Column(db.Integer)

    lecture_student = db.relationship("LectureStudents", back_populates="grades")
