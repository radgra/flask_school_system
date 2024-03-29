from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.users import UserList, UserLogin
from resources.teachers import TeacherList, TeacherDetail, AssignAzubis
from resources.students import StudentList, StudentDetail
from resources.lectures import LectureList, LectureDetail, AssignStudents
from resources.lecture_students import LectureStudentsList, LectureStudentsDetail
from resources.grades import GradeList, GradeDetail
from marshmallow import ValidationError
from sqlalchemy import exc
from ma import ma
from utils.permissions import PermissionAccessException

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JSON_SORT_KEYS'] = False

app.secret_key = 'sdkjlsajdkslaj' #app.config['JWT_SECRET_KEY']
api = Api(app)

from db import db
db.init_app(app)
ma.init_app(app)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()

# like a except blof
@app.errorhandler(ValidationError)
def handle_marshmallow_validation(error):
    print("ole")
    return jsonify(error.messages), 400



@app.errorhandler(Exception)
def handle_error(e):
    print(e)
    return jsonify({"message": "Something went wrong"}), 500

@app.errorhandler(PermissionAccessException)
def handle_permission_error(e):
    return jsonify({"message":"You have no permission to do that"})

@app.errorhandler(exc.IntegrityError)
def handle_integrity_error(e):
    return jsonify({"message": e.args[0]}), 500


# users
api.add_resource(UserList, '/users')
api.add_resource(UserLogin, '/login')

# teachers
api.add_resource(TeacherList, '/teachers')
api.add_resource(TeacherDetail, '/teachers/<int:id>')
api.add_resource(AssignAzubis, '/teachers/<int:id>/assign_azubis')

# students
api.add_resource(StudentList, '/students')
api.add_resource(StudentDetail, '/students/<int:id>')

# lectures
api.add_resource(LectureList, '/lectures')
api.add_resource(LectureDetail, '/lectures/<int:id>')
api.add_resource(AssignStudents, '/lectures/<int:id>/students')

# lecture_students
api.add_resource(LectureStudentsList, '/lecturestudents')
api.add_resource(LectureStudentsDetail, '/lecturestudents/<int:id>')

# grades
api.add_resource(GradeList,'/grades')
api.add_resource(GradeDetail,'/grades/<int:id>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
