import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from models.student import Student
from db import db
from flask import Flask
from seeding_data import teachers, users
from models.teacher import Teacher
from models.user import UserModel
from shell_start import seed_all
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()

class TestTeacher(unittest.TestCase):
    
    def setUp(self):
        self.db = SQLAlchemy()
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # Dynamically bind SQLAlchemy to application
        self.db.init_app(self.app)
        self.app.app_context().push()
        #self.db.drop_all()
        #self.db.create_all()
        seed_all(self.db)



    def test_self_refernce_azubi(self):
        keith = Teacher.query.filter_by(is_ausbildung=True).first()
        self.assertEqual(keith.ausbilder.user.username, 'jagger')

        jagger = Teacher.query.filter(Teacher.user.has(username="jagger")).first()
        self.assertEqual(jagger.azubis[0].user.username, 'keith')


    # def test_deleting_ausbilder(self):
    #     jagger = Teacher.query.filter(Teacher.user.has(username="jagger")).first()
    #     self.db.session.delete(jagger)
    #     self.db.session.commit()
    #     # Check if user exists - it should
    #     self.assertTrue(UserModel.query.filter_by(username="jagger"),True)

    #     keith = Teacher.query.filter_by(is_ausbildung=True).first()
    #     self.assertEqual(keith.ausbilder, None)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

