# W.A.P to calculate emi

# p = principal amount 
# R = Rate of Interest
# N = Number of months
# Equation :-
# EMI = [P×R×(1+R)^N] / [(1+R)^N−1]

p = 10000
r= 15
n = 12
emi = (p*r*(1+r)**n)// ((1+r)**n-1)
print("EMI Amount is :", emi)