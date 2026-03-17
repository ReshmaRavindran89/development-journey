def analyze_numbers(*args,**kwargs):

    if kwargs.get("action")=="max":

        return max(args)
    
    if kwargs.get("action")=="min":

        return min(args)
    
    if kwargs.get("action")=="count":

        return len(args)
    
print(analyze_numbers(10,20,30,40,50,action = "max"))
print(analyze_numbers(10,20,30,40,50,action = "min"))
print(analyze_numbers(10,20,30,40,50,action = "count"))

