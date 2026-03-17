class Student:

    def __init__(self,name,course,roll_number):

        self.name = name
        self.course = course
        self.roll_number = roll_number

    def display(self):

        print(self.name,self.course,self.roll_number)

student_instance1 = Student("vipin","MCA",15)
student_instance1.display()
