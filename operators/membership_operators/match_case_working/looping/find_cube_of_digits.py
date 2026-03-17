# find cube of digit
# number=123 ,3**3,2**3,1**3

number = 123
sum=0
while(number!=0): # 123!=0,
    last_digit = number%10 
    cube = last_digit**3
    sum = sum + cube
    number= number//10
print(sum)
