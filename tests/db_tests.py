import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from models.student import Student


Base = declarative_base()

class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = Session(engine)
        Base.metadata.create_all(engine)

        for teacher in teachers:
            user = UserModel.query.filter_by(username=teacher.pop('username')).first()

            if teacher['is_ausbildung'] == True:
                ausbilder = UserModel.query.filter_by(username=teacher.pop('ausbilder')).first()
                if ausbilder:
                    teacher['ausbilder_id'] = ausbilder.id
            
            if user:
                new_teacher = Teacher(**teacher, user_id=user.id)
                self.session.add(new_teacher)
                self.session.commit()