
# write a program to check the list is positive_list ,negative_list.

numbers = [-1,-1,10,11,12,13,-15,4,5]
positive_list = []
negative_list = []

for num in numbers:
    if num>0:
        positive_list.append(num)
    else:
        negative_list.append(num)
        
print("postive",positive_list)
print("negative",negative_list)
