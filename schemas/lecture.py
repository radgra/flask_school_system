from ma import ma
from models.lecture import Lecture
from marshmallow import fields, validates, ValidationError,  validates_schema, Schema
from schemas.teacher import TeacherSchema

class LectureSchema(ma.ModelSchema):
    teacher = fields.Nested(TeacherSchema, exclude=('lectures','azubis','ausbilder'))
    class Meta:
        model = Lecture
        include_fk = True

    # required/nullable fields sa automatycznie validated

    # unique constraint najlepiej narazie tak zrobic:
    # 1. na modelu unique i pozwolic sqlalchemy raise error
    # 2. na schema zrobic validator
    # 3. Jak kiedys performance bedzie wazne to pomyslimy
    @validates('topic')
    def validate_unique_topic(self, value):
        if self.instance and self.instance.topic == value:
            return
            
        topic = Lecture.query.filter_by(topic=value).first()
        if topic:
            raise ValidationError("Such topic already exists")

        return True


class AssignStudentsSchema(Schema):
    students = fields.List(fields.Integer, required=True)

