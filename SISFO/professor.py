from base.User import User

class Professor(User):
    def __init__(self, user_id, name, email, password, faculty_id):
        super().__init__(user_id, name, email, password)
        self.faculty_id = faculty_id
        self.courses_taught = []
        self.nilai = []        

    def teach_course(self, course):
        self.courses_taught.append(course)
        
    


