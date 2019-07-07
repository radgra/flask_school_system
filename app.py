from flask import Flask
from flask_restful import Api
from resources.users import UserList
from resources.teachers import TeacherList, TeacherDetail, AssignAzubis
from ma import ma

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'sdkjlsajdkslaj'
api = Api(app)

from db import db
db.init_app(app)
ma.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(UserList, '/users')
api.add_resource(TeacherList, '/teachers')
api.add_resource(TeacherDetail, '/teachers/<int:id>')
api.add_resource(AssignAzubis, '/teachers/<int:id>/assign_azubis')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
