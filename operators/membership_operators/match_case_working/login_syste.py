# W.A.P 

# if password is correct:
#  ask OTP
# if OTP is correct -> "Login Successful"
# Else -> "Incorrect OTP"
# Else -> "Incorrect Password"

db_password = "password@123"
db_otp = "2121"
user_password = input("Enter Password: ")
if db_password==user_password:
        user_otp = int(input("Enter otp:"))

if db_password ==user_otp:
        
        print(" Login Successful")

else:
        print(" Incorrect OTP")

    