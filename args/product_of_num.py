
def product_of_num(*args:tuple):

    product = 1

    for num in args:

        product = product * num

    return product
    
print(product_of_num(1,2,3)) # 6
print(product_of_num(1,2,3,4)) # 24
print(product_of_num(1,2,3,4,5)) # 120


# list comprehension :-

