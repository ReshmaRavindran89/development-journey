# Login successful or not


username = "admin"
password = "1234"

user_input = input("Enter username: ")
pass_input = input("Enter password: ")

if user_input == username and pass_input == password:
    print("Login successful")
else:
    print("Login failed")