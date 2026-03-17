
# Write a program to count how many times a given number appears in a list.

nums = [1, 2, 3, 2, 4, 2, 5]

n = 2
count = 0

for i in nums:

    if i == n:
        count += 1

print(n ,"appears" ,count ,"times")