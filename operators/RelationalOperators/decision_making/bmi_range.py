# bmi range calculation

weight_in_kg = int(input("Enter weight in kg: "))
height_in_cm = int(input("Enter height in cm: "))
height_in_m = height_in_cm/100
bmi = weight_in_kg/(height_in_m**2)
bmi = round(bmi)
print(bmi)
if bmi<20:
    print(" UNDERWEIGHT")
elif bmi<25:
    print(" NORMAL")
elif bmi<30:
    print(" OVERWEIGHT")
else:
    print(" OBESE")
    