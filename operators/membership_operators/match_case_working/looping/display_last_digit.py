# Display last digit
# floor

number = int(input("Enter Number: ")) #123
while(number!=0): # 123!=0,# 12!=0,1!=0
    last_digit = number%10 # 3,2,1,0
    print(last_digit) # 3,2,1,0
    number = number//10 # 123//10=12,12//10=1,1//10=0
