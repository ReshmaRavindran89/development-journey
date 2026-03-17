# Cholesterol Level Check
# Input: cholesterol
# Conditions:

# If cholesterol < 200 → Desirable

# If cholesterol between 200 and 239 → Borderline High

# If cholesterol ≥ 240 → High Cholesterol

cholestrol = int(input("Enter Cholestrol Level: "))
if cholestrol<200:
    print(" Desirable")
elif cholestrol<239:
    print(" Borderline High")
else:
    print(" High Cholesterol")
    