
"""
   set

 *  Union
 *  Intersection
 *  Difference

"""

set_a = {10,20,30,40,50,60,80}
set_b = {40,50,20,}

u_set = set_a.union(set_b)
print("Union Set",u_set)

i_set = set_a.intersection(set_b)
print("Intersection",i_set)

d_set = set_a.difference(set_b)
print("Difference",d_set)

print(set_a.issuperset(set_b)) # true
print(set_b.issubset(set_a)) # true

