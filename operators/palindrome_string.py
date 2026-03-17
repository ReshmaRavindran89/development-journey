
# palindrome string

word = input("Enter String: ")

word_length = len(word)-1

result = ""

for i in range(word_length,-1,-1):

    result = result + word[i]
    
if result == word:

    print("Palindrome")

else:

    print("Not Palindrome")

