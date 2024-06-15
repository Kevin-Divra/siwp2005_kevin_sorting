class User:
    def __init__(self, user_id, name, email, password):
        self._user_id = user_id  # Encapsulation: Private attribute
        self._name = name
        self._email = email
        self._password = password

    def login(self, email, password):  # Abstraction: Login method
        if email == self._email and password == self._password:
            #continue the logic here
            return True
        else:
            return False

    def get_user_id(self):  # Encapsulation: Accessor method
        return self._user_id
