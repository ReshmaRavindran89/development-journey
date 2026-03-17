# Print the multiplication table of given number using a while loop
number =int(input("Enter Number: "))
i = 1
while i <= 10:
    result =number *i
    print(f"{number} x {i} = {result}")
    i += 1
