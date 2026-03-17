"""
error => zero division error
         index error
         file not found
         key error

"""

age = int(input("enter age"))

if age<18:

    raise Exception("invalid age")

else:

    print("access granted")

