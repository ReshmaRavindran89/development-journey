"""
W.A.P to find factorial of any given number.
"""
num = int(input("Enter the Factorial: "))
i = 1
result = 1
while(i<=num): # 1<=4,2<=4....,4<=4
    result = result*i # 1,.....4
    i= i+1 # 1+1=2,...,4
print(num,"Factorial is ",result) # 
