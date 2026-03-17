
# slicing list:-

# slicing[start:stop:step]

lst = [10,20,30,40,50,60]

#       0  1  2  3  4  5

portion = lst[0:4]
print(portion)

portion2 = lst[2:]
print(portion2)

portion3 = lst[:5]
print(portion3)

lst_copy = lst[::]  #  here we get exact copy of the list  by using [::]
print(lst_copy)
