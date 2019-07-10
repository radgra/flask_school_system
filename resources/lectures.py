from flask_restful import Resource
from models.lecture import Lecture
from schemas.lecture import LectureSchema, AssignStudentsSchema
from marshmallow import ValidationError 
from models.student import Student
from models.lecture_students import LectureStudents
from flask import request
from db import db


class LectureList(Resource):
    lecture_schema = LectureSchema()
    
    def get(self):
        lectures = Lecture.query.all()

        data = self.lecture_schema.dump(lectures, many=True)

        return {"data":data}

    def post(self):
        lecture_update_schema = LectureSchema(exclude=('id','teacher','students'))
        data = request.get_json()

        new_lecture = lecture_update_schema.load(data)
        db.session.add(new_lecture)
        db.session.commit()


        return {'data':self.lecture_schema.dump(new_lecture)}


class LectureDetail(Resource):
    lecture_schema = LectureSchema()

    def get(self,id):
        lecture = Lecture.query.get(id)
        if lecture is None:
            return {"message":"Lecture with such id doesnt exist."}
        
        return {"data":self.lecture_schema.dump(lecture)}


    def patch(self,id):
        lecture = Lecture.query.get(id)
        if lecture is None:
            return {"message":"Lecture with such id doesnt exist."}
        
        lecture_update_schema = LectureSchema(exclude=('id','teacher','students'), partial=True)
        data = request.get_json()
        updated_lecture = lecture_update_schema.load(data, instance=lecture)
        
        db.session.commit()

        return {"data":self.lecture_schema.dump(updated_lecture)}

    def delete(self, id):
        lecture = Lecture.query.get(id)
        if lecture is None:
            return {"message":"Lecture with such id doesnt exist."}
        
        db.session.delete(lecture)
        db.session.commit()

        return {"message":"Lecture deleted."}


class AssignStudents(Resource):
    def patch(self,id):
        full_schema = LectureSchema()
        assign_students_schema = AssignStudentsSchema()
        data = request.get_json()
        lecture = Lecture.query.get(id)
        if lecture is None:
            return {"messge":"Lecture not found"}

        
        student_ids = assign_students_schema.load(data)

        # jak zbudowac to query
        # to mozna preloading lectures
        students = Student.query.filter(Student.id.in_(student_ids["students"])).all()
        for student in students:
            lectures = [lect for lect in student.lectures if lect.lecture_id == lecture.id]
            # Bulk create student_id/lecture_id ??
            if not lectures:
                lecture_student = LectureStudents()
                lecture_student.lecture = lecture
                student.lectures.append(lecture_student)

            # przeszukac student.lectures czy maja juz 
        

        db.session.commit()

        # To musze inaczej zrobic
        # mam studentow - muzse znalezsc tych studentow ktorzy nie maja lecture assigned

        
        return {"data":full_schema.dump(lecture)}
