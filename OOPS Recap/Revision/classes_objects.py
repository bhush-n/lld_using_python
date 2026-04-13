class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating objects of the Student class
student1 = Student("Bhushan", 24)
student1.display()
