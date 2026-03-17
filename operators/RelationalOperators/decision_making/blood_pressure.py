# Write a Python program using if elif else to print the health status.
# Blood Pressure Category
#Input: systolic_bp
#Conditions:
#If bp < 120 → Normal
#If bp between 120 and 129 → Elevated
#If bp between 130 and 139 → High BP Stage 1
#If bp >= 140 → High BP Stage 2

systolic_bp = int(input("Enter the blood pressure: "))
if systolic_bp<120:
    print(" NORMAL")
elif systolic_bp<129:
    print(" ELEVATED")
elif systolic_bp<139:
    print(" HIGH BP STAGE 1")
else:
    print(" HIGH BP STAGE 2")
    
