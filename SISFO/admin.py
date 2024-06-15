from base.User import User
from student import Student
from professor import Professor
#continue other user here

class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    """
        encapsulates the functionality required to create user accounts
        This ensures that all details about how user accounts are instantiated, 
        such as initializing user properties and setting initial states 
        or conditions, are kept within the Admin class. This prevents 
        the object's internal state from being tampered with 
        or accessed directly from outside the class methods, 
        adhering to data hiding principles.
    """
    def create_user_account(self, user_type, *args):
        # Polymorphism
        if user_type == "student":
            return Student(*args)
        elif user_type == "professor":
            return Professor(*args)
        elif user_type == "operator":
            pass
        else:
            return None