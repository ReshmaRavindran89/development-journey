

# def sort()

numbers = [12,1,13,14,15]
numbers.sort() # by default Ascending Order.
print(numbers)

colors = ["red","white","blue","black"]
colors.sort()
print(colors)

# def sort(self,reverse =false)

numbers = [12,1,13,14,15]
numbers.sort(reverse=True) # Descending Order.
print(numbers)


# def reverse() => rotate the list.

colors = ["red","white","blue","black"]
colors.reverse()
print(colors)

# def extend(self,iterable)

colors = ["red","white","blue","black"]
new_colors = ["cyan","brown","purple"]
colors.extend(new_colors)
print(colors)

# if we use append instead of extend.

colors = ["red","white","blue","black"]
new_colors = ["cyan","brown","purple"]
colors.append(new_colors)
print(colors)