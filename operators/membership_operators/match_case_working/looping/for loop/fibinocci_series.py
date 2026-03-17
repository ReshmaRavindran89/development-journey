
# fibinocci series:-

prev = 0 
curr = 1
print(prev)
print(curr)

# print(prev,curr)

for i in range(1,14):
    next = prev + curr # 0+1 =1, 1+1=2,....
    print(next)
    prev = curr
    curr = next

