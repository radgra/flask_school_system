from flask_restful import Resource
from models.lecture_students import LectureStudents
from schemas.lecture_students import LectureStudentsSchema
from marshmallow import ValidationError 
from flask import request
from db import db


class LectureStudentsList(Resource):
    # This works too !!!!!! Cool !!!!
    lecture_students_schema = LectureStudentsSchema()
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


class LectureStudentsDetail(Resource):
    lecture_students_schema = LectureStudentsSchema()
    
    def get(self,id):
        lecture_student = LectureStudents.query.get(id)
        if lecture_student is None:
            return {"message":"There is no resource with such id"}

        return {"data":self.lecture_students_schema.dump(lecture_student)}

    def patch(self,id):
        lecture_student = LectureStudents.query.get(id)
        if lecture_student is None:
            return {"message":"There is no resource with such id"}

        lecture_student_update_schema = LectureStudentsSchema(only=('student_id','lecture_id','final_grade'))
        data = request.get_json()
        updated_lecture = lecture_student_update_schema.load(data, instance=lecture_student, partial=True)

        db.session.commit()

        return {"data":self.lecture_students_schema.dump(updated_lecture)}


    def delete(self,id):
        lecture_student = LectureStudents.query.get(id)
        if lecture_student is None:
            return {"message":"There is no resource with such id"}

        db.session.delete(lecture_student)
        db.session.commit()

        return {"message":"Resource deleted."}


    