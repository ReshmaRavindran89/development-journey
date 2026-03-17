
# Write a program to find the smallest element in a list.

nums = [10, 21, 4, 45, 66, 93]

smallest = nums[0]

for i in nums:

    if i < smallest:
        smallest = i

print("Smallest:", smallest)
