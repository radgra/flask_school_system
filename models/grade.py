from db import db


class Grade(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True)
    lecture_student_id = db.Column(db.Integer, db.ForeignKey("lecture_students.id"), nullable=False)
    grade = db.Column(db.Integer, nullable=False)

    lecture_student = db.relationship("LectureStudents", back_populates="grades")



# Gdzie to chce miec
# 1 separate endpoint - lecture id/student id/grade
# 2 musi by validacja czy student is assigned to lecture
# 3 bulk assigning of grades - on student/id/lectures/id/grades <- two ids

# Czy lepszy model to direct foreign key czy dwa foeign key to student and lecture ?
# Mozge zrobic custom schema ->


# Jak validuje foreign keys?
# Foreign keys nie sa przestrzegane  - i tak sam musze je walidowac
