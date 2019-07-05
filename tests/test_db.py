import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from models.teacher import Teacher
from models.user import UserModel
from seeding_data import teachers
from app import app
from db import db
from flask import Flask

Base = declarative_base()

class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.init_app(self.app)
        
        app.app_context().push() 
        db.create_all()
        self.populate_db()
    
    def populate_db(self):
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

    def testSomething(self):

        print(Teacher.query.all())
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()