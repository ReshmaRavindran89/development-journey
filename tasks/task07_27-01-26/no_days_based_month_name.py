# 10. Write a program using match–case to print the number of days in a month.
#  based on the month name.

month = input("Enter the Month: ")
match month:
    case "january":
        print(" 31 Days")
    case "february":
        print(" 28 Days or 29 Days in a leap year")
    case "march":
        print(" 31 Days")
    case "april":  
        print(" 30 Days")
    case "may":
        print(" 31 Days") 
    case "june":
        print(" 30 Days") 
    case "july":
        print(" 31 Days") 
    case "august":
        print(" 31 Days") 
    case "september":
        print(" 30 Days") 
    case "october":
        print(" 31 Days") 
    case "november":
        print(" 30 Days") 
    case "december":
        print(" 31 Days") 
    case _:
        print("Invalid Month") 