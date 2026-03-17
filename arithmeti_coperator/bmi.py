# W.A.P TO FIND BMI(BODYMASSINDEX)
# Equation   bni weight_in_kg / (height_in_meter)^2

h_in_cm = 165 #height in cm = 165
w_in_kg = 56  #weight in kg = 56
h_in_m = h_in_cm/100 #height in meter = 165/100 = 1.65
bmi = w_in_kg/(h_in_m**2) #bmi = 56/1.65**2
print(bmi)