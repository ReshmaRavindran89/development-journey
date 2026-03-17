
# Attendence Store:-
# sunday to Monday 
# H => holiday
# P => present
# O => online

attendence_store = ["H","P","P","P","P","P","H"]
                #    0   1   2   3   4   5   6
print(attendence_store)

# thursday = holiday (thursday value in to hiliday)

attendence_store[4] = "H"
print(attendence_store)

for at in attendence_store:
    print(at)
