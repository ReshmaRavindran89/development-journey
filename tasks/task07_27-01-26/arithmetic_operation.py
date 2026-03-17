# 3. Create a menu-driven program using match–case for basic arithmetic operations:
# * 1 → Addition
# * 2 → Subtraction
# * 3 → Multiplication
# * 4 → Division

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
operation = input("enter the operation: ")
match operation:
    case "+":
        print("addition", num1+num2)
    case "-":
        print("subtraction", num1-num2)
    case "*":
        print("multiplication",num1*num2)
    case "/":
        print("division", num1/num2)
    case "%":
        print("mod",num1%num2)
    case "//":
        print("floor",num1//num2)
    case "**":
        print("expo",num1**num2)
    case _:
        print("invalid operation")
        
