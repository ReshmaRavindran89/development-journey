def calculator(*args,**kwargs):


    if kwargs.get("key")=="+":
        
        return sum(args)
    
    if kwargs.get("key")=="*":

        product = 1

        for num in args:

            product = product * num

        return product
    
print(calculator(10,20,30,40,key = "+"))
print(calculator(10,20,30,40,key = "*"))

