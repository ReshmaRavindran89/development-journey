# 1st Question Task 07 check day and print based on a number.
# 
# W.A.P  using match–case to display the day of the week based on a number (1–7).


day = int(input("enter Day: "))
match day:
    case 1:
        print("SUN")
    case 2:
        print("MON")
    case 3:
        print("TUE")
    case 4:
        print("WED")
    case 5:
        print("THU")
    case 6:
        print("FRI")
    case 7:
        print("SAT")
    case _:
        print("INVALID")