from base.User import User

#contoh Student inherit dari User
class Student(User):
    def __init__(self, user_id, name, email, password, enrollment_id):
        super().__init__(user_id, name, email, password)
        self.enrollment_id = enrollment_id
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)
        course.add_student(self)

