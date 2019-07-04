from db import db

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    wage = db.Column(db.Integer)
    is_ausbildung = db.Column(db.Boolean, default=False)
    ausbilder_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    
    user = db.relationship("UserModel", back_populates="teacher")
    azubi = db.relationship('Teacher', backref=db.backref('ausbilder', remote_side=[id]))
    lectures = db.relationship('Lecture', back_populates="teacher")

    def __repr__(self):
        return self.user.username
