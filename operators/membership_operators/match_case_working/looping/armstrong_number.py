# check whether the number is armstrong or not.

number = int(input("Enter Number: "))
number_copy = number
result = 0
number_length = len(str(number))
while(number!=0):
    digit = number%10
    expo = digit**number_length
    result = result + expo
    number = number//10
if number_copy ==result:
        print("Armstrong Number")
else:
        
        print( "Not an Armstrong Number")
        