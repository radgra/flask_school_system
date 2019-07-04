from models.user import UserModel
from models.student import Student
from models.teacher import Teacher
from models.lecture_students import LectureStudents
from models.lecture import Lecture
from models.grade import Grade
from db import db 
from app import app
from seeding_data import users, students, teachers

db.init_app(app)


def run_shell():
    app.app_context().push()
    # nie kasuje db
    db.create_all()


def seed_users():
    with app.app_context():
        db.create_all()
        for user in users:
            new_user = UserModel(**user)
            db.session.add(new_user)
            db.session.commit()

def seed_students():
    with app.app_context():
        for student in students:
            user = UserModel.query.filter_by(username=student.pop('username')).first()
            print(student)
            if user:
                new_student = Student(**student, user_id=user.id)
                db.session.add(new_student)
                db.session.commit()


def seed_teachers():
    with app.app_context():
        for teacher in teachers:
            user = UserModel.query.filter_by(username=teacher.pop('username')).first()

            if teacher['is_ausbildung'] == True:
                ausbilder = UserModel.query.filter_by(username=teacher.pop('ausbilder')).first()
                if ausbilder:
                    teacher['ausbilder_id'] = ausbilder.id
            
            if user:
                new_teacher = Teacher(**teacher, user_id=user.id)
                db.session.add(new_teacher)
                db.session.commit()


def seed_all():
    seed_users()
    seed_students()
    seed_teachers()



            