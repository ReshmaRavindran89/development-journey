
"""

   *   
  * *
 * * *
* * * *
 * * *
  * *
   *
Diamond Pattern 

"""
def diamond(n):
    # Part 1: Top half (including the widest middle row)
    for i in range(1, n + 1):
        # Calculate spaces: total height minus current row
        spaces = " " * (n - i)
        # Calculate stars: 2n - 1 logic
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    # Part 2: Bottom half (starts from n-1 down to 1)
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Let's print a diamond with a radius of 5
diamond(6)