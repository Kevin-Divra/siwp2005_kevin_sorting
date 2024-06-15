class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.students_enrolled = []  # List of Student objects
        self.course_materials = []

    def add_student(self, student):
        self.students_enrolled.append(student)
