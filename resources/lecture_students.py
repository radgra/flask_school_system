from flask_restful import Resource
from models.lecture_students import LectureStudents
from schemas.lecture_students import LectureStudentsSchema
from marshmallow import ValidationError 
from flask import request
from db import db


class LectureStudentsResource(Resource):
    lecture_students_schema = LectureStudentsSchema()
    def get(self):
        lecture_students = LectureStudents.query.all()

        return {"data":lecture_students_schema.dump(lecture_students)}
