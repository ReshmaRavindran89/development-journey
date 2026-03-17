# Display rating
# Display unsatisfied rating <4.0
# Display neutral rating >=4.0 and <4.5
# Display satisfied rating >=4.5

rating = float(input("Enter Rating: "))
if rating<4.0:
    print(" unsatisfied")
elif rating>=4.0 and rating<4.5:
    print(" Neutral")
else:
    print(" satisfied")