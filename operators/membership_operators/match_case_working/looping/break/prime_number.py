
# check given number is prime number or not

number = int(input("Enter Number: ")) # 7
is_prime = True # true
for i in range(2,number): # 2,...,6
    if number%i==0: #  7%2==0,7%3==0,.....7%6==0
        is_prime = False
        break
print(is_prime) #  true
