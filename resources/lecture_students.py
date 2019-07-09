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


    def post(self):
        lecture_students_update_schema = LectureStudentsSchema(only=("lecture_id","student_id","final_grade"))
        data = request.get_json()

        new_lecture_student = lecture_students_update_schema.load(data)
        db.session.add(new_lecture_student)
        db.session.commit()

        return {"data":self.lecture_students_schema.dump(new_lecture_student)}
