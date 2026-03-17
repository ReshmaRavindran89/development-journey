# Write a Python program to check whether a given year is a leap year.


year = int(input("Enter the Year: "))
if year%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")
