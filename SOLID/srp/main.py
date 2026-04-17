# in this file we will define the main function to demonstrate the usage of the User class and its methods.
from user import User
from user_operation import UserOperation


user1 = User("john_doe", "john@email.com", "password123")
user_operation = UserOperation()


user_operation.save_user(user1)
user_operation.delete_user(user1)
