from ma import ma
from models.lecture import Lecture
from models.lecture_students import LectureStudents
from marshmallow import fields, validates, ValidationError,  validates_schema, Schema
from schemas.teacher import TeacherSchema


class LectureStudentsSchema(ma.ModelSchema):
    class Meta:
        model = LectureStudents
        include_fk = True
        


