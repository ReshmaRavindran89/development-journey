"""
read a password
length of password is <6 create custom error is password invalid.

"""
password = (input("enter password"))

if len(password) <6:

    raise Exception("password invalid")

else:

    print("password correct")