from db import db
from sqlalchemy.orm import validates, backref

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    started = db.Column(db.Date)
    age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), unique=True, nullable=False)
    
    user = db.relationship("UserModel", backref=backref('student', passive_deletes=False, uselist=False, cascade="all, delete-orphan"))
    #lectures = db.relationship('LectureStudents', back_populates="student")

    def __repr__(self):
        return self.user.username

