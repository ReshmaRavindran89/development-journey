# Body Temperature Status

# Input: body_temperature (°C)
# Conditions:

# If temperature < 36 → Low Body Temperature

# If temperature between 36 and 37.5 → Normal

# If temperature > 37.5 → Fever

body_temperature = float(input("Enter Body Temperature: "))
if body_temperature<36:
    print(" LOW BODY TEMPERATURE")
elif body_temperature<=37.5:
    print(" NORMAL")
else:
    print(" Fever")
    
