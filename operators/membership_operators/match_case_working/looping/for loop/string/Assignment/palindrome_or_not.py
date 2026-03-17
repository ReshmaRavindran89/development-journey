
# Write a program to check whether a list is a palindrome.

nums = [1, 2, 3, 2, 1]

if nums == nums[::-1]:

    print("It is a palindrome")

else:
    
    print("Not a palindrome")