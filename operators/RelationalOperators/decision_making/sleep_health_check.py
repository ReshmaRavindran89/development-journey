# Sleep Duration Health Check
# Input: hours_of_sleep
# Conditions:
# If sleep < 6 → Sleep Deprived
# If sleep between 6 and 8 → Healthy Sleep
# If sleep > 8 → Oversleeping

hours_of_sleep = int(input("Enter the hours of sleep: "))
if hours_of_sleep<6:
    print(" SLEEP DEPRIVED")
elif hours_of_sleep<8:
    print(" HEALTHY SLEEP")
else:
    print(" OVERSLEEP")
    
