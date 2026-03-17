# 12. Write a program to check whether a given character is uppercase or lowercase.

character = input("Enter a character: ")

if character >= 'A' and character <= 'Z':

    print("UPPERCASE")

elif character >= 'a' and character <= 'z':

    print("lowercase")

else:
    
    print("Not a letter")

