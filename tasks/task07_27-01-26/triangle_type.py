# 4.Write a program using match–case to print the type of triangle based on a given input:
# * "e" → Equilateral
# * "i" → Isosceles
# * "s" → Scalene

triangle_type = input("Enter triangle Type: ")
match triangle_type:
    case "e":
        print(" Equilateral")
    case "i":
        print(" Isosceles")
    case "s":
        print(" Scalene")
    case _:
        print(" invalid Triangle Type")
        
