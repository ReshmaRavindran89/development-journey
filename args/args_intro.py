"""
*args -> receives any number of parameter as tuple.

"""

def add(*args):

    return sum(args)

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))

def largest_number(*args):

    return max(args)

print(largest_number(10,20))
print(largest_number(10,20,30,40,50))



    