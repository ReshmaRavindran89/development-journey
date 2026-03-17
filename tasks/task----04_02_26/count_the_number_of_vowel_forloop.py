
# Count the number of vowels in a given string using a for loop.

text = "Hello World"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

