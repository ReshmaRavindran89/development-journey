# number = 1234
# Display count of digit.

number = 1234
count = 0
while(number!=0): # 1234!=0,
    last_digit = number%10 # 1234%10=4,
    count = count + 1 # 
    number = number//10
print(count)

