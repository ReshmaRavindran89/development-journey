
# Write a program to print factorial of a number using for loop.

number = int(input("Enter the Number: "))
fact = 1
for i in range(1,number+1):
    fact = fact * i
print(f"factorial of number is {number} is {fact}")

