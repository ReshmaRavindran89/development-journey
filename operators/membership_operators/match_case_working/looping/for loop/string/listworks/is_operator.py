"""
# is opreator :-
 => identity operator checks whether 2 variables are pointing same memory location or not.
"""

akash_fvt_colors = ["red","white","blue","black"]

sreyesh_fvt_colors = akash_fvt_colors.copy()
print(akash_fvt_colors is sreyesh_fvt_colors)

print(akash_fvt_colors==sreyesh_fvt_colors) # true == value compare.
print(akash_fvt_colors is sreyesh_fvt_colors) # false is memory location compare.

