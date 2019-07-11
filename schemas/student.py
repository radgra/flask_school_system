from ma import ma
from models.student import Student
from schemas.user import UserSchema
from marshmallow import fields, validates, ValidationError,  validates_schema, Schema
from models.user import UserModel
from schemas.user import UserSchema


class StudentSchema(ma.ModelSchema):
    user = fields.Nested(UserSchema,exclude=('password',))
    class Meta:
        model = Student
        include_fk = True
        dump_only = ('id', 'user', 'lecture_students')
        ordered = True
        

    @validates('user_id')
    def validate_user_id(self, value):
        if self.instance and self.instance.user_id == value:
            return
            
        user = UserModel.query.get(value)
        if user is None:
            raise ValidationError("User with such Id doesnt exist.")
        
        if(user.teacher or user.student):
            raise ValidationError("User with such Id is already assigned.")

        return True

