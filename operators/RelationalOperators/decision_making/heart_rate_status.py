# Heart Rate Status
# Input: heart_rate (beats per minute)
# Conditions:
# If heart_rate < 60 → Low Heart Rate
#If heart_rate between 60 and 100 → Normal
# If heart_rate > 100 → High Heart Rate

heart_rate = int(input("Enter the heart rate: "))
if heart_rate<60:
    print(" LOW HEART RATE: ")
elif heart_rate<100:
    print(" NORMAL")
else:
    print(" HIGH HEART RATE")
    