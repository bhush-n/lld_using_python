# create the UserOperation class in this repo to handle user-related operations such as registration, login, and password reset. This class should have methods to perform these operations and should use the User class to manage user data.

from user import User


class UserOperation:
    def __init__(self):
        self.users = {}

    def save_user(self, User: User):
        print(f"Saving user: {User._username}")

    def delete_user(self, User: User):
        print(f"Deleting user: {User._username}")
