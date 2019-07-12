from flask_restful import Resource
from models.grade import Grade
from models.lecture_students import LectureStudents
from schemas.grade import GradeSchema, GradeCreateSchema
from models.lecture import Lecture
from schemas.lecture import LectureSchema, AssignStudentsSchema
from marshmallow import ValidationError 
from models.student import Student
from models.lecture_students import LectureStudents
from flask import request
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import UserModel
from utils.permissions import check_object_permission




class GradeList(Resource):
    grade_schema  = GradeSchema()

    def get(self):
        grades = Grade.query.all()

        data = self.grade_schema.dump(grades, many=True)

        return {"data":data}

    @jwt_required
    def post(self):
        data = request.get_json()
        
        # moge to tez w funkcji zamknac np checkPermission i raise custom error ktory zlapie na poziomie app
        


        grade_create_schema = GradeCreateSchema()
        grade = grade_create_schema.load(data)

        lecture_student = LectureStudents.query.filter_by(lecture_id=grade["lecture_id"],student_id=grade["student_id"]).first()
        if lecture_student is None:
            return {"mesage":"This student is not assigned to this lecture"}


        current_user_id = get_jwt_identity()
        #current_user = UserModel.query.get(current_user_id)
        teacher_id =  lecture_student.lecture.teacher_id
        if current_user_id != teacher_id:
            return {"You have no permission to do that"}

        new_grade = Grade()
        new_grade.lecture_student = lecture_student
        new_grade.grade = grade['grade']

        db.session.add(new_grade)
        db.session.commit()

        return {"data":self.grade_schema.dump(new_grade)}


class GradeDetail(Resource):
    grade_schema  = GradeSchema()

    @jwt_required
    def get(self,id):
        grade = Grade.query.get(id)
        if grade is None:
            return {"message":"Grade with such id doesnt exist."}

        # Handling Permission
        user_id =  grade.lecture_student.lecture.teacher.user_id
        check_object_permission(user_id)

        # wnioski - permissons na objektach lepiej zamykac w funkcje ktore raisuja error - ng generalna check_object_permission
        # w przypadku skomplikowanej logiki moge przeniesc to przeciez do private method ktore zajmie sie pewna czescia logiki a route handler bedzie czysty
        # decorators - wtedy kiedy permission lezy na user model np is_admin itd

        return {"data":self.grade_schema.dump(grade)}


    def patch(self,id):
        grade = Grade.query.get(id)
        data = request.get_json()
        if grade is None:
            return {"message":"Grade with such id doesnt exist."}

        grade_update_schema = GradeSchema(only=("grade",))
        updated_grade = grade_update_schema.load(data, instance=grade)
        
        db.session.commit()
        return {"data":self.grade_schema.dump(updated_grade)}


    def delete(self,id):
        grade = Grade.query.get(id)
        if grade is None:
            return {"message":"Grade with such id doesnt exist."}

        db.session.delete(grade)
        db.session.commit()

        return {"message":"Grade deleted"}


# Na jutro
# Endpoint lecture/id/students/id/grades - bulk assigning - problem with date - should i allow that ? - in real app i wouldnt do that !
# TODO importannt:
# testing - postman or flask - after my api is ready i should know whether it works and consider all features..... think about testing
# JWT_extended without refresh token in this app - next time i will use refresh token

# Permissions:
#   - only teacher who is assigned to lecture should be able to change/add grades
#   - only admin should be able to add teachers to lecture
#   - only certain student should be able to view his/hers own grades

# Na jutro - JWT_extended and permissions
# Na koncu password hashing - zeby to rozdielic