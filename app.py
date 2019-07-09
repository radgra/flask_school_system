from flask import Flask, jsonify
from flask_restful import Api
from resources.users import UserList
from resources.teachers import TeacherList, TeacherDetail, AssignAzubis
from resources.students import StudentList, StudentDetail
from resources.lectures import LectureList, LectureDetail
from resources.lecture_students import LectureStudentsResource
from marshmallow import ValidationError
from sqlalchemy import exc
from ma import ma

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JSON_SORT_KEYS'] = False

app.secret_key = 'sdkjlsajdkslaj'
api = Api(app)

from db import db
db.init_app(app)
ma.init_app(app)


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

@app.errorhandler(exc.IntegrityError)
def handle_error(e):
    return jsonify({"message": e.args[0]}), 500


# users
api.add_resource(UserList, '/users')

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

# lecture_students
api.add_resource(LectureStudentsResource, '/lecturestudents')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
