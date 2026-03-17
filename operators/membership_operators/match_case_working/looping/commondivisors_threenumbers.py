


num1 = int(input("Enter num1: "))

num2 = int(input("Enter num2: "))

num3 = int(input("Enter num3: "))


if num1 <= num2 and num1 <= num3:

    smallest_number = num1

elif num2 <= num1 and num2 <=num3:

    smallest_number = num2

else:

    smallest_number = num3

print("The common divisors of three numbers are: ")


for i in range(1, smallest_number + 1):

    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:

        print(i)

