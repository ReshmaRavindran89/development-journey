# Stress Level Indicator
# Input: stress_score (1 to 10)
# Conditions:
# If score between 1 and 3 → Low Stress
# If score between 4 and 6 → Moderate Stress
# If score between 7 and 10 → High Stress

stress_code = int(input("Enter stress score: "))
if stress_code<3:
    print(" LOW STRESS")
elif stress_code<6:
    print(" MODERATE STRESS")
else:
    print(" HIGH STRESS")

