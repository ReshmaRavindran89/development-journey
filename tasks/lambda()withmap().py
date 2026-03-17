
# 5. Use a lambda function with map() 

lst = [10,11,12,13,14,15]

map_squares = list(map(lambda n:n**2,lst))
print(map_squares)

# list comprehension :-

com_squares = [num**2 for num in lst]
print(com_squares)


