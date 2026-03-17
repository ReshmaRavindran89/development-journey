
# Use a lambda function with filter() to get all even numbers from a list.

lst = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda n:n%2==0,lst))
print(even)

# Using list comprehension:-

even_com = [num for num in lst if num%2==0]
print(even_com)

