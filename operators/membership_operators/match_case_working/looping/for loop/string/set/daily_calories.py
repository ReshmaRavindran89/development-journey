
# Daily calories :-

daily_calories = {
    "sun":2300,
    "mon":1600,
    "tue":1800,
    "wed":1500,
    "thu":1900,
    "fri":1900,
    "sat":2000,
}

for key in daily_calories:
    print(key,daily_calories[key])

# Total Calories:- 

total_calories = 0

for key in daily_calories:

    cal = daily_calories[key]
    total_calories+=cal

print(total_calories)

# to find average calorie:-

avg_calorie = total_calories/len(daily_calories)
print(avg_calorie)

