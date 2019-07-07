from ma import ma
from models.teacher import Teacher
from schemas.user import UserSchema
from marshmallow import fields, validates, ValidationError,  validates_schema, Schema
from models.user import UserModel

class TeacherSchema(ma.ModelSchema):
    user = fields.Nested(UserSchema, exclude=("password",))
    azubis_ids = fields.Pluck('self', 'id', attribute="azubis",many=True)
    azubis = fields.Nested('self', attribute="azubis",many=True, dump_only=True, exclude=['azubis','azubis_ids'])
    
    class Meta:
        model = Teacher
        include_fk = True
        dump_only = ('azubis','user')

    # Cos takiego znalazlem
    # students = fields.List(fields.Nested(StudentSchema))
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

    @validates('ausbilder_id')
    def validate_ausbilder_id(self,value):
        if self.instance and self.instance.id == value:
            raise ValidationError("Ausbilder must have diffrent id that Student.")


    @validates_schema
    def validate_is_ausbildung(self,data,**kwargs):
        print(data)
        is_ausbildung = data.get('is_ausbildung') 
        if is_ausbildung is None:
            return True

        ausbilder_id =  data.get('ausbilder_id')
        if ausbilder_id is None:
            raise ValidationError("Ausbilder Id is required.")
        
        ausbilder = Teacher.query.get(ausbilder_id)
        if ausbilder is None:
            raise ValidationError("Asubilder with such id doesnt exit.")


class TeacherSchemaAssignAzubis(Schema):
    azubis = fields.List(fields.Integer, required=True)

    @validates('azubis')
    def validate_id_not_in_azubis(self,value,**kwargs):
        if self.context['teacher_id'] in value:
            raise ValidationError("Error from Marshmellow.")


        print(value)
        return True
