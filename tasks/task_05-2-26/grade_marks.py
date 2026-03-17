
# 3. Write a program to print the grade based on marks:
"""
90 and above → A
75–89 → B
50–74 → C
Below 50 → Fail

"""

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")