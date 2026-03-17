
fr =open("file operators\\foods_logs.txt")

food_logs = []

for line in fr:
   
   # line = "1,break_fast,idly,175,11-1-2025,hari"

   data = line.rstrip("\n").split(",") # [1,meal_type,name,calorie,date,owner]

   log ={"id":data[0],"meal_type":data[1],"name":data[2],"calorie":float(data[3]),"date":data[4],"owner":data[5]}

   food_logs.append(log)
   
print(food_logs)
