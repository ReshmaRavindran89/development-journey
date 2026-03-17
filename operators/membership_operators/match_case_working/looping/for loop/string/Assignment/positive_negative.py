
#  Write a program to count positive and negative numbers in a list.

nums = [10, -2, 5, -8, 0, -1]

pos = 0
neg = 0

for i in nums:

    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1

print("Positives:", pos)
print("Negatives:", neg)
