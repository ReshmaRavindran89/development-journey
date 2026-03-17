
# Write a program to print the list in reverse order (without using reverse method).

nums = [1, 2, 3, 4, 5]

# using a loop:

for i in range(len(nums)-1, -1, -1):

    print(nums[i], end=" ")
