from db import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    started = db.Columns(db.Date)
    age = db.Columns(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship("User", back_populates="teacher")
    lectures = db.relationship('LectureStudents', back_populates="student")

