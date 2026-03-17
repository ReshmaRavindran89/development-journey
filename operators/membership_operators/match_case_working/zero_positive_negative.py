
# Write a program to check whether a given number is positive, negative, or zero.

number = int(input("Enter Number: "))
match number:
    case 0:
        print(" Zero")
    case _ if number<0:
        print(" Negative")
    case _ if number>0:
        print(" Positive")
    case _:
        print(" Invalid")


