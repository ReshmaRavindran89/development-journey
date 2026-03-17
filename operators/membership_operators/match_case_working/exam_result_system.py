"""
5. Exam Result System
------------------------------------
Task:
- Ask for roll number

If roll number exists:
    - Ask for marks
    - If marks ≥ 40:
        "Pass"
    - Else:
        "Fail"
Else:
    "Invalid roll number"
"""

roll_no = int(input("Roll Number: "))
marks = int(input("Marks: "))

if roll_no == 101 and marks >= 40:
    print("Pass")
elif roll_no == 101 and marks < 40:
    print("Fail")
else:
    print("Invalid roll number")
    