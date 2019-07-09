from ma import ma
from models.lecture import Lecture
from models.lecture_students import LectureStudents
from marshmallow import fields, validates, ValidationError,  validates_schema, Schema
from schemas.student import StudentSchema
from schemas.lecture import LectureSchema

class LectureStudentsSchema(ma.ModelSchema):
    student = fields.Nested(StudentSchema, exclude=('user_id','lectures'))
    # Mozna nested excludes !
    lecture = fields.Nested(LectureSchema, exclude=('students','teacher.user_id'))
    class Meta:
        model = LectureStudents
        include_fk = True



