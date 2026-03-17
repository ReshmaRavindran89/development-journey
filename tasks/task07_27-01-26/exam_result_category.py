
""" Write a program to determine exam result category.
* Marks ≥ 90 → Distinction
* Marks ≥ 60 → First class
* Marks ≥ 40 → Pass
* Below 40 → Fail
"""


marks = int(input("Enter your marks: "))

# Check categories from highest to lowest
if marks >= 90:

    print("Result: Distinction")

elif marks >= 60:

    print("Result: First class")

elif marks >= 40:

    print("Result: Pass")

else:
    
    print("Result: Fail")
