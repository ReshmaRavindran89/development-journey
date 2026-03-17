# 11. Write a program to check whether a number is greater than 100 or not.

number = float(input("Enter a number: "))
is_greater = number > 100
match is_greater:
    case True:
        print(" is greater than 100")
    case False:
        print(f" is not greater than 100")
        