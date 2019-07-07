from flask_restful import Resource
from models.teacher import Teacher
from schemas.teacher import TeacherSchema, TeacherSchemaAssignAzubis
from marshmallow import ValidationError 
from flask import request
from db import db

class TeacherList(Resource):
    def get(self):
        teacher_schema = TeacherSchema(exclude=('ausbilder',))
        teachers = Teacher.query.all()
        data = teacher_schema.dump(teachers, many=True)
        return {
            "data":data
        }

    
    def post(self):
        # TODO handle unique user_id
        teacher_schema = TeacherSchema()
        data = request.get_json()
        try:
            new_teacher = teacher_schema.load(data)
            db.session.add(new_teacher)
            db.session.commit()
        except ValidationError as err:
            return err.messages, 400


        return {"data":teacher_schema.dump(new_teacher)}


class TeacherDetail(Resource):
    def get(self, id):
        teacher_schema = TeacherSchema()
        teacher = Teacher.query.get(id)
        # w grunice rzeczy sluzy jako metoda do json w getach
        data = teacher_schema.dump(teacher)
        return {
            "data":data
        }

    def patch(self, id):
        teacher_schema = TeacherSchema(only=("wage","user_id","ausbilder_id"),partial=True)
        data = request.get_json()
        teacher = Teacher.query.get(id)
        if teacher is None:
            return {"messge":"Teacher not found"}
        try:
            updated_teacher = teacher_schema.load(data, instance=teacher)
        except ValidationError as err:
            return err.messages, 400
        
        return {"data":teacher_schema.dump(updated_teacher)}



class AssignAzubis(Resource):
    def patch(self,id):
        full_schema = TeacherSchema()
        teacher_schema = TeacherSchemaAssignAzubis(context={'teacher_id': id})
        data = request.get_json()
        teacher = Teacher.query.get(id)
        if teacher is None:
            return {"messge":"Teacher not found"}

        try:
            azubis_ids = teacher_schema.load(data)
            # przenislem to do marshmallow
            if id in azubis_ids['azubis']:
                return {"error":"You cannot assign ausbilder to themselves"}

            azubis = Teacher.query.filter(Teacher.id.in_(azubis_ids['azubis'])).all()
            teacher.azubis = azubis
            db.session.commit()

        except ValidationError as err:
            return err.messages, 400
        
        return {"data":full_schema.dump(teacher)}







