
"""
Display Duplicates

"""
numbers =[10,10,20,30,10,40,50,60,30,10]

st = set() # here we use set => to add numbers without duplicates.

for num in numbers:

    num_count = numbers.count(num) # 

    if num_count>1:
        st.add(num)

print(st)

