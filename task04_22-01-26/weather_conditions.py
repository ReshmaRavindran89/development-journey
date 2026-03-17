# Write a Python program to display weather conditions based on temperature:

# Above 30 → Hot
# 20 to 30 → Warm
# Below 20 → Cold

temperature = int(input("Enter Temperature: "))
if temperature>30:
    print(" HOT")
elif temperature>=20:
    print(" WARM")
else:
    print(" COLD")
