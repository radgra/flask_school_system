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

    @validates_schema
    def validate_unique(self,data,**kwargs):
        student_id = data.get('student_id')
        lecture_id = data.get('lecture_id')
        lk_exist = LectureStudents.query.filter_by(student_id=student_id, lecture_id=lecture_id).first()
        if lk_exist:
            raise ValidationError("Fields lecture_id and student_id should be unique together")

        return True