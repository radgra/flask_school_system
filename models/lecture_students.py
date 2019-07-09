from db import db


class LectureStudents(db.Model):
    __tablename__ = 'lecture_students'
    __table_args__ = (
        db.UniqueConstraint('lecture_id', 'student_id', name='unique_lecture_student'),
    )

    id = db.Column(db.Integer, primary_key=True)
    lecture_id = db.Column(db.Integer, db.ForeignKey('lectures.id', ondelete='CASCADE'))    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id', ondelete='CASCADE'))
    final_grade = db.Column(db.Integer, nullable=True)

    student = db.relationship("Student", back_populates="lectures")
    lecture = db.relationship("Lecture", back_populates="students")
    grades = db.relationship("Grade", back_populates="lecture_student")

    # Do i need 'passive_deletes' for on_delete=Cascade ?
    # https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete

# lecture student - have to be unique together ! - po zbudowaniu endpointa


# Potrzebuje nastepujace endpointy:
# 1 Bulk partial update - only student_id - if exist dont delete it cause of final_grade <---- zeby sprawdzic czy to bedzie dzialalo narazie musze zbudwac endpoint ktory pozwoli dawanie gradow
# 2 Assigning single student to lecture - could be done on student endpoint or separate endpoint - must have update/delete/patch capabilities FOR EXERICSE DO BOTH
# 3 Test deleteing student and lecture - If on delete cascade works !!!
