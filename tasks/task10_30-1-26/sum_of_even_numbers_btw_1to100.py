

"""
sum of even numbers btw 1 to 100.
"""
number = 2
total_sum = 0

while number <= 100:
    total_sum += number  # Add the current even number to the total
    number += 2          # Jump to the next even number

print("The sum of even numbers from 1 to 100 is:", total_sum)

