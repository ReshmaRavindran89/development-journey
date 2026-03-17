
# Write a program to count the number of digits in a given number using a while loop.

number = 12345
count = 0


number_copy = number

if number_copy == 0:
    count = 1
else:
    while number_copy > 0:
        number_copy = number_copy // 10  # This removes the last digit
        count += 1        

print("Number of digits:", count)