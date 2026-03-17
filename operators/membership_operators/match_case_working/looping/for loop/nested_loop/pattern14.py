
"""
*****
 ****
  ***
   **
    * 

"""


for i in range(5, 0, -1):
    # Calculate spaces: Total rows minus current stars
    spaces = " " * (5- i)
    stars = "*" * i
    print(spaces + stars)
    