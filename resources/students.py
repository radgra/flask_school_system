from flask_restful import Resource
from models.student import Student
from schemas.student import StudentSchema
from marshmallow import ValidationError 
from flask import request
from db import db
from sqlalchemy import desc

class StudentList(Resource):
    def get(self):
        student_schema = StudentSchema()
        students = Student.query.order_by(desc("started")).all() #works with dates
        
        data = student_schema.dump(students, many=True)
        
        return {"data":data}

    def post(self):
        student_schema = StudentSchema()
        data = request.get_json()

        new_student = student_schema.load(data)
        db.session.add(new_student)
        db.session.commit()

        return {"data":student_schema.dump(new_student)}


class StudentDetail(Resource):
    student_schema = StudentSchema()
    def _get_student(id):
        # Tutaj moge wyszukac studenta i go zwrocic - jesli go nie znajde raise custom error z messagem np raise ObjectNotFound,
        # i przechwycic go w app - dry code !  
        pass

    def get(self, id):
        student = Student.query.get(id)
        if student is None:
            return {"messge":"Student not found"}
        data = self.student_schema.dump(student)
        return {
            "data":data
        }

    def patch(self, id):
        student_update_schema = StudentSchema(only=('age','user_id','started'), partial=True)
        student = Student.query.get(id)
        if student is None:
            return {"messge":"Student not found"}

        data = request.get_json()
        updated_student =  student_update_schema.load(data, instance=student)
        db.session.commit()

        return {
            "data":self.student_schema.dump(updated_student)
        }

    def delete(self, id):
        student = Student.query.get(id)
        if student is None:
            return {"messge":"Student not found"}

        # tu musze miec pewnosc ze student zawsze ma usera
        db.session.delete(student.user)
        db.session.commit()

        return {"message":"Object deleted"}


# TODOS - Think later about assigning after i bulid lecture and grade endpoints
# 1. Assigning lectures - later after lectures endpoint 

