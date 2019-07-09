from flask_restful import Resource
from models.lecture_students import LectureStudents
from schemas.lecture_students import LectureStudentsSchema
from marshmallow import ValidationError 
from flask import request
from db import db


class LectureStudentsResource(Resource):
    # This works too !!!!!! Cool !!!!
    lecture_students_schema = LectureStudentsSchema(exclude=('student.user.id',))
    def get(self):
        lecture_students = LectureStudents.query.all()

        return {"data":self.lecture_students_schema.dump(lecture_students, many=True)}
