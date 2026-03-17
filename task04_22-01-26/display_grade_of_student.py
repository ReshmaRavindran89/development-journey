# Write a Python program to display the grade of a student using the following rules:

# Marks ≥ 90 → Grade A
# Marks ≥ 75 → Grade B
# Marks ≥ 50 → Grade C
# Otherwise → Fail


marks= int(input("Enter Marks: "))
if marks>=90:
    print("  Grade A")
elif marks>=75:
    print(  "Grade B")
elif marks>=50:
    print("  Grade c")
else:
    print("  Fail")

    