# Body Mass Index (BMI) Category

# Input: bmi
# Conditions:

# If bmi < 18.5 → Underweight

# If bmi between 18.5 and 24.9 → Normal Weight

# If bmi between 25 and 29.9 → Overweight

# If bmi ≥ 30 → Obese

weight_in_kg = float(input("Enter weight in kg: "))
height_in_cm = float(input("Enter height in cm: "))
height_in_m = height_in_cm/100
bmi = weight_in_kg/(height_in_m**2)
round(bmi)
print(bmi)
if bmi<18.5:
    print(" UNDER WEIGHT")
elif bmi<24.9:
    print(" NORMAL WEIGHT")
elif bmi<29.9:
    print(" OVER WEIGHT")
else:
    print(" OBESE")
