from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_teacher = db.Column(db.Boolean, default=False)

    student = db.relationship("Student", uselist=False, back_populates="user")
    #teacher = db.relationship("Teacher", uselist=False, passive_deletes=True, back_populates="user")
    #teacher = db.relationship("Teacher", uselist=False, passive_deletes=True, cascade="all, delete", back_populates="user") #That works


    def __repr__(self):
        return self.username

    def json(self):
        return {
            "id":self.id,
            "username":self.username,
        }

    # multifield validation
    def validate(self):
        pass
    