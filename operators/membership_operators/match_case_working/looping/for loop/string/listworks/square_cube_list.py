
# write a program to create two list square_list and cube_list.

numbers = [2,3,4,5,6,12,13]
square_list = []
cube_list =[]
for num in numbers:
    square = num**2
    cube = num**3
    square_list.append(square)
    cube_list.append(cube)
    
print("square",square_list)
print("cube",cube_list)

