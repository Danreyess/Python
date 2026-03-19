class Student:
    def __init__(self, name: str, age:int, major: str):
        self.name = name #Attribute
        self.age = age #Attribute
        self.major = major #Attribute
        self.courses = [] #Default attribute

        # A Method (a function inside a class)
    def enroll (self, course_name: str):
            self.courses.append(course_name)
            print(f"{self.name} is now enrolled in {course_name}")
#Creating an "Instance" (Object)
luis = Student("Luis", 4, "Data Scientist Engineer")
luis.enroll("Discrete Mathematics")
