
#  Write a Python program to sort a list of tuples based on the second element using a lambda function.

students = [
    ("hari",145),
    ("rishi",135),
    ("vipi",125),
    ("sri",175),
    ("kavi",165),
]

print(sorted(students,key=lambda tp:tp[1]))  

# for descending order:-

print(sorted(students,key=lambda tp:tp[1],reverse=True)) 

# 
