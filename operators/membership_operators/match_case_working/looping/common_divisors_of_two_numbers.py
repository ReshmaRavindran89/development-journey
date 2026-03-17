
# write a program to display common divisors of two numbers

num1 = int(input("Enter num1: "))

num2 = int(input("Enter num2: "))

if num1<num2:

    smallest_number = num1

else:

    smallest_number = num2

    print("The common divisors are:")

    for i in range(1,smallest_number+1):

        if num1%i==0 and num2%i==0:

            print(i)


