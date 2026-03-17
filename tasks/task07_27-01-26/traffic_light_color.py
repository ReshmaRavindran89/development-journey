# 6. Write a program that takes a traffic light color as input .
# prints the corresponding action using match–case.

light_color = input("Enter the traffic Light Color: ")
match light_color:
    case "red":
        print(" STOP")
    case "yellow":
        print(" WAIT")
    case "green":
        print(" GO")
    case _:
        print(" Invalid Color")