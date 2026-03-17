#  Age Group Classification

# Input: age
# Conditions:

# If age < 13 → Child

# If age between 13 and 19 → Teenager

# If age between 20 and 59 → Adult

# If age ≥ 60 → Senior Citizen

age = int(input("Enter the Age: "))
if age<13:
    print(" CHILD")
elif age<19:
    print(" TEENAGER")
elif age<59:
    print(" ADULT")
else:
    print(" SENIOR CITIZEN")
    