
# Write a program to count how many odd and even numbers are present in a list.

nums = [1, 2, 3, 4, 5, 6]

even_count = 0
odd_count = 0

for i in nums:

    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Evens:", even_count)
print("Odds:", odd_count)

