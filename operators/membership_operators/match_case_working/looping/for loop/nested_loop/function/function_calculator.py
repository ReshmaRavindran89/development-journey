# create a function calculator with n1,n2,op.

def calculator(n1,n2,op):
    if op=="+":
        return n1+n2 
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        return n1/n2
    
print(calculator(10,5,"+"))
