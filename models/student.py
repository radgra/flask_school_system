from db import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    started = db.Column(db.Date)
    age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    
    user = db.relationship("UserModel", back_populates="student")
    lectures = db.relationship('LectureStudents', back_populates="student")

    def __repr__(self):
        return self.user.username

