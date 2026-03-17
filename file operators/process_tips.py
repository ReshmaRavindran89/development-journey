
from csv import DictReader

fr = open("file operators\\tips.csv")

# csv => list_of_diction [csv.py => DictReader]

data = list(DictReader(fr)) # print list of dictionary
print(data)

# day_wise_summary = {sun:345,mon:345}

day_wise_summary = {}

for d in data:

    tip = float(d.get("tip"))

    day = d.get("day")

    if day in day_wise_summary:

        day_wise_summary[day]+=tip

    else:

        day_wise_summary[day] = tip

print(day_wise_summary)


# day_with_highest_revenue:-

day_wise_total = {}

for d in data:
   
    day = d.get("day")
   
    total_bill = float(d.get("total_bill"))

    if day in day_wise_total:
      
     
        day_wise_total[day]+=total_bill

    else:
      
        day_wise_total[day]=total_bill

print(day_wise_total)
   
    
#  who gave more tips (male or female):-

height_tip = {}
for d in data:
    tip = float(d.get("tip"))
    gender = 