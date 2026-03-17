# read fasting blood sugar

fasting_blood_sugar = int(input("Enter the blood sugar: "))
if fasting_blood_sugar<100:
    print(" NORMAL")
elif fasting_blood_sugar<125:
    print(" PREDIABETS")
else:
    print(" DIABETS")
