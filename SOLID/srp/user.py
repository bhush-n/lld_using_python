# define the User class in this repo to represent a user in the system. This class should have attributes such as username, email, and password, and methods to get and set these attributes.class User:


class User:
    def __init__(self, username: str, email: str, password: str):
        self._username = username
        self._email = email
        self._password = password
