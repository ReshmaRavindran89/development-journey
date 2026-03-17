

attendence = ["H","P","P","P","P","P","H"]
                #    0   1   2   3   4   5 


holiday_count = 0
present_count = 0

for att in attendence:

    if att =="H":

        holiday_count+=1

    elif att =="p":
         
         present_count+=1

print("holiday count",holiday_count)
print("present count",present_count)
