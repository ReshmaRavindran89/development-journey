# 5) Daily Water Intake

# Input: liters
# Conditions:

# If intake < 2 → Dehydrated

# If intake between 2 and 3 → Adequate Intake

# If intake > 3 → Excess Intake

litres= float(input("Enter liters: "))
if litres<2:
    print(" Dehydrated")
elif litres<3:
    print(" Adequate Intake")
else:
    print(" Excess intake")
    
    