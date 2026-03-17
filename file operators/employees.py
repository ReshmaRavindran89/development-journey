employees = ["hari","dixon","rahul","vysakh","sreejith"]

# write in file operation:-

fw = open("file operators\\employees.txt","w")

for e in employees:
    fw.write(e+"\n")

print("completed.......")


# append in file operation:-

fa = open("file operators\\employees.txt","a")

for e in employees:
    fw.write(e+"\n")

print("completed.......")



