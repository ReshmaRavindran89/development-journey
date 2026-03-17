
# palindrome or not.

number = int(input("Enter number"))
number_copy = number
result = 0
while(number!=0):

    digit = number%10
    result = result*10+digit
    number = number//10

if result == number_copy:
        
        print(" Palindrome")

else:
        
        print(" Not Palindrome")

 