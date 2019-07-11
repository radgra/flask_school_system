from ma import ma
from models.lecture import Lecture
from marshmallow import fields, validates, ValidationError,  validates_schema, Schema
from models.grade import Grade


class GradeSchema(ma.ModelSchema):
    lecture_id = fields.Integer(attribute="lecture_student.lecture_id", dump_only=True)
    student_id = fields.Integer(attribute="lecture_student.student_id", dump_only=True)
    class Meta:
        model = Grade
        include_fk = True
        exclude = ("lecture_student",)


class GradeCreateSchema(Schema):
    student_id = fields.Integer(required=True)
    lecture_id = fields.Integer(required=True)
    grade  = fields.Integer(required=True)