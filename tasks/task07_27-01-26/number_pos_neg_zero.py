# 7. Write a program using match–case to check whether a given number is;
#  positive, negative, or zero.


number = float(input("Enter a number: "))

match number:
    case n if n > 0:
        print("Number is POSITIVE")
    case n if n < 0:
        print("Number is NEGATIVE")
    case 0:
        print("Number is ZERO")
    case _:
        print("Invalid input")