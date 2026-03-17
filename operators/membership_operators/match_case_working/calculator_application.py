# create calculator Application
# read num1 , num2 ,and operation

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
operation = input("enter the operation: ")
match operation:
    case "+":
        print("add", num1+num2)
    case "-":
        print("sub", num1-num2)
    case "*":
        print("mul",num1*num2)
    case "/":
        print("div", num1/num2)
    case "%":
        print("mod",num1%num2)
    case "//":
        print("floor",num1//num2)
    case "**":
        print("expo",num1**num2)
    case _:
        print("invalid operation")
