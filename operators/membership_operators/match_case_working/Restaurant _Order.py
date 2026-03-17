"""
 Restaurant Order System
------------------------------------
Task:
- Ask for table number

If table exists:
    - Ask for food availability
    - If food available:
        "Order placed"
    - Else:
        "Item out of stock"
Else:
    "Invalid table number"
"""
table_number = int(input("Enter table number: "))

if table_number < 1 or table_number > 10:
    print("Invalid table number")
else:
    food_item = input("Enter food item: ")
    if food_item == "Pasta":
        print("Order placed")
    else:
        print("Item out of stock")