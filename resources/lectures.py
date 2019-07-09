from flask_restful import Resource
from models.lecture import Lecture
from schemas.lecture import LectureSchema
from marshmallow import ValidationError 
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