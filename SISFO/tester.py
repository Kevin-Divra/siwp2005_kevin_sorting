from admin import Admin
from courses import Course

def main():
    admin = Admin("A1", "Monica", "monica@si.ukrida.ac.id", "adminpass")

    # instantiate
    """
    args:
        - user type: "student or professor"
        - user_id, name, email, and password for user object
        - enrollment_id for student object
        - faculty_id for professor object
        example: 
        - ("user_type", "user_id", "name", "email", "password","enrollment_id")
        - admin.create_user_account("student", "S1", "peter", "peter@si.ukrida.ac.id", "studentpass", "E1234")
    """
    student = admin.create_user_account("student", "S1", "peter", "peter@si.ukrida.ac.id", "studentpass", "E1234")
    student1 = admin.create_user_account("student", "S2", "jesica", "jesica@si.ukrida.ac.id", "studentpass1", "testtest")
    professor = admin.create_user_account("professor", "P1", "Dr. Endi", "example@ukrida.ac.id", "profpass", "F5678")

    # Courses
    dsp_course = Course("siwp1001", "Algorithma", "Introduction to programing and algorithms fundamental")
    pbo_course = Course("siwp2005", "PBO", "object oriented programming")

    #Enroll student and assign professor
    if student:
        student.enroll_in_course(dsp_course)
    if student1:
        student1.enroll_in_course(pbo_course)
    if professor:
        professor.teach_course(pbo_course)

    # Polymorphism
    for user in [student, student1, professor]:
        if user:
            print(f"User {user.get_user_id()} can log in: {user.login(user._email, 'studentpass')}")

if __name__ == "__main__":
    main()
