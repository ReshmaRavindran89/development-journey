
#  Write a program to find the largest element in a list.

nums = [10, 21, 4, 45, 66, 93]

largest = nums[0]

for i in nums:

    if i > largest:
        largest = i

print("Largest:", largest)
