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
    grades = db.relationship("Grades", back_populates="lecture_student")

    # Do i need 'passive_deletes' for on_delete=Cascade ?
    # https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete