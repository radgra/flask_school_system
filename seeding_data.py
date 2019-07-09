import datetime

users = [
    {
        "username":"macca",
        "password":"1234",
        "is_teacher":False
    },
    {
        "username":"lennon",
        "password":"1234",
        "is_teacher":False
    },
    {
        "username":"ringo",
        "password":"1234",
        "is_teacher":False
    },
    {
        "username":"harrison",
        "password":"1234",
        "is_teacher":True
    },
    {
        "username":"jagger",
        "password":"1234",
        "is_teacher":True
    },
    {
        "username":"keith",
        "password":"1234",
        "is_teacher":True,
    },
]

students = [
    {   "username":"lennon",
        "age":30,
        "started":datetime.datetime(2015, 5, 17)
    },
    {   
        "username":"macca",
        "age":20,
        "started":datetime.datetime(2012, 3, 10)
    },
    {   
        "username":"ringo",
        "age":25,
        "started":datetime.datetime(2016, 10, 30)
    }
]

teachers = [
    {
        "username":"harrison",
        "wage":12323,
        "is_ausbildung":False,
        
    },
    {
        "username":"jagger",
        "wage":12323,
        "is_ausbildung":False,

    },
    {
        "username":"keith",
        "ausbilder":"jagger",
        "wage":12323,
        "is_ausbildung":True,

    },
    # {
    #     "wage":12323,
    #     "is_ausbildung":True,

    # }
]

lectures = [
    {
        "teacher_id":1,
        "topic":"Math"
    },
    {
        "teacher_id":2,
        "topic":"English"
    },
    {
        "teacher_id":3,
        "topic":"Politics"
    },
]


lecture_students = [
    {
        "lecture_id":1,
        "student_id":1,
        "final_grade":2
    },
    {
        "lecture_id":1,
        "student_id":2,
        "final_grade":1
    },
    {
        "lecture_id":1,
        "student_id":3,
        "final_grade":3
    },
    {
        "lecture_id":2,
        "student_id":2
    },
    {
        "lecture_id":2,
        "student_id":3
    },
    {
        "lecture_id":3,
        "student_id":1
    },
]