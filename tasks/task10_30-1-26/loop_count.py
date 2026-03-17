
# Write a Python program to count how many times a loop runs when printing numbers from 
# 1 to 20 using a while loop.

number = 1

count = 0

# The loop runs as long as number is less than or equal to 20

while number <= 20:

    print(f"Current number: {number}")
    
    number += 1
    count += 1

print("-" * 20)

print(f"Total number of times loop runs: {count}")