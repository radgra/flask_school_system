from db import db
from sqlalchemy.orm import validates, backref

class LectureStudents(db.Model):
    __tablename__ = 'lecture_students'
    # WORKS !
    __table_args__ = (
        db.UniqueConstraint('lecture_id', 'student_id', name='unique_lecture_student'),
    )

    id = db.Column(db.Integer, primary_key=True)
    lecture_id = db.Column(db.Integer, db.ForeignKey('lectures.id', ondelete='CASCADE'), nullable=False)    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    final_grade = db.Column(db.Integer, nullable=True)

    student = db.relationship("Student",backref=backref('lectures', passive_deletes=False, cascade="all, delete-orphan"))
    lecture = db.relationship("Lecture",backref=backref('students', passive_deletes=False, cascade="all, delete-orphan"))
    grades = db.relationship("Grade", back_populates="lecture_student")

    # Do i need 'passive_deletes' for on_delete=Cascade ?
    # https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete

### First to do ######################################
# lecture student - have to be unique together ! - po zbudowaniu endpointa <--------- WORKS and DONE


# Potrzebuje nastepujace endpointy:
# 1 Bulk partial update - only student_id - if exist dont delete it cause of final_grade <---- zeby sprawdzic czy to bedzie dzialalo narazie musze zbudwac endpoint ktory pozwoli dawanie gradow
# 2 Assigning single student to lecture - could be done on student endpoint or separate endpoint - must have update/delete/patch capabilities FOR EXERICSE DO BOTH
# 3 Test deleteing student and lecture - If on delete cascade works !!!

# NEXT STEPS:
# 1. Test ondelete cascade - student and lecture
# 2. Finish endpoint - detail/patch/delete
# 3. Try Bulk Update - if it works


# Maly Problem :
# Przy M2M lecture_students - both lecture->students i students->lecture wskazuje id tabeli posredniej a nie bezposrednio do wlasciwego resource. Rozwiazania:
# 1. zmienic na lecture_students
# 2. dodac dodatkowa propoerty na schema students/lecture i zmappowac id
# 3. bezposrednio zmappowac na modelu relacje - ale i tak chce miec final_grade
# 4. czy mouna nested fields jako main fields