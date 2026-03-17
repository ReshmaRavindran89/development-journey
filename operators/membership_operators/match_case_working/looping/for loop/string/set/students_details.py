
"""
student details:-

id
name
course
marks

tasks:-
print student name.

"""

student_details = {"id":1234,"name":"yash","course":"python","marks":79}
print(student_details["name"])

# update mark adding 5 bonus.

student_details["marks"]+=5
student_details["grade"]="A"
print(student_details)

if "attendence" in student_details:
    print("yes")
else:nji8
    print("no")
