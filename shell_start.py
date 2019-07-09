from models.user import UserModel
from models.student import Student
from models.teacher import Teacher
from models.lecture_students import LectureStudents
from models.lecture import Lecture
from models.grade import Grade
from db import db 
from app import app
from seeding_data import users, students, teachers, lectures, lecture_students

db.init_app(app)


def run_shell():
    app.app_context().push()
    # nie kasuje db
    db.create_all()


def seed_users(_db):
        _db.create_all()
        for user in users:
            new_user = UserModel(**user)
            db.session.add(new_user)
            db.session.commit()

def seed_students(db):
        _students = list(students)
        print(_students)
        for stud in _students:
            student  = stud.copy()
            user = UserModel.query.filter_by(username=student.get('username')).first()

            if user:
                student.pop('username')
                new_student = Student(**student, user_id=user.id)
                db.session.add(new_student)
                db.session.commit()


def seed_teachers(db):
        for teach in teachers:
            teacher = teach.copy()
            user = UserModel.query.filter_by(username=teacher.pop('username')).first()

            if teacher['is_ausbildung'] == True:
                ausbilder = Teacher.query.filter(Teacher.user.has(username=teacher['ausbilder'])).first()
                if ausbilder:
                    teacher['ausbilder'] = ausbilder
            
            if user:
                new_teacher = Teacher(**teacher, user_id=user.id)
                db.session.add(new_teacher)
                db.session.commit()


def seed_lectures():
    for lecture in lectures:
        new_lecture = Lecture(**lecture)
        db.session.add(new_lecture)
        db.session.commit()


def seed_lecture_students():
    for ls in lecture_students:
        new_ls = LectureStudents(**ls)
        db.session.add(new_ls)
        db.session.commit()



def seed_all(_db=db):
    seed_users(_db)
    seed_students(_db)
    seed_teachers(_db)
    seed_lectures()
    seed_lecture_students()


            