
# Write a program to find the second largest element in a list (without sorting).

nums = [10, 45, 4, 45, 66, 93, 93]

max = secondmax = 0

for i in nums:

    if i > max:

        secondmax = max
        max = i

    elif i > secondmax and i != max:
        secondmax = i

print("Second Largest:", secondmax)



