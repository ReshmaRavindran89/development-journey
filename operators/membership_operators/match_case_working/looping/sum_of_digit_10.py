# number = 123
# sum of digit 10

number = 123
sum =0
while(number!=0): # 123!=0,12!=0,1!=0
    last_digit = number%10 # 123%10=3,2,1
    sum = sum+last_digit # sum = 0+3=3+2=>5+1=6
    number = number//10 # 12//10=1=0
print(sum)
