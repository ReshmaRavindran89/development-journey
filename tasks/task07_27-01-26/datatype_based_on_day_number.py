



day = int(input("Enter day number: "))


if day >= 1 and day <= 5:

    print(day, "is a Working day")

elif day == 6 or day == 7:

    print(day, "is a Weekend")

else:
    
    print("Invalid input! Please enter a number between 1 and 7.")