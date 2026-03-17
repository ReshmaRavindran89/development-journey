# read a number
# check number is / by 8
# yes : display number is divisible by 8
# No : display number is not divisible by 8

number = int(input("Enter the Number: "))
if number%8==0: # 16%8==0 
    print("Divisible by 8")
else:
    print("Not Divisible by 8")
    