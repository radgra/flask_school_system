from db import db
from sqlalchemy.orm import validates, backref
from sqlalchemy import event

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    wage = db.Column(db.Integer)
    is_ausbildung = db.Column(db.Boolean, default=False)
    ausbilder_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), unique=True, nullable=False)
    # FOR SQLITE passive_deletes must be set to False !!!!!! Otherwise it wont work - it will delete user but wont change foreign key on teacher
    user = db.relationship("UserModel", backref=backref('teacher', passive_deletes=False, uselist=False, cascade="all, delete-orphan")) 
    azubi = db.relationship('Teacher', backref=db.backref('ausbilder', remote_side=[id]))
    lectures = db.relationship('Lecture', back_populates="teacher")

    def __repr__(self):
        return self.user.username

    def validate(self):
        if self.user.is_teacher is False:
            return False

        if self.is_ausbildung is True and self.ausbilder is None:
            return False
        
        return True


    # Property sqlalchemy validation - ONLY FOR DEMO
    @validates('wage')
    def validate_user(self, key, address):
        print(key)
        print(address)
        return address





# Validation for setting user attribute - ONLY FOR DEMO
@event.listens_for(Teacher.user, 'set', retval=True)
def validate_obj(target, value, oldvalue, initiator):
    print('event fired for validate_obj')
    print(value)
    return value