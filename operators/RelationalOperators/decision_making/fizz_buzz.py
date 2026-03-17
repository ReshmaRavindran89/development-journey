# w.A.P TO CHECK FIZZBUZZ
# DISPLAY FIZZ DIVISIBLE / 3
# DISPLAY BUZZ DIVISIBLE / 5
# DISPLAY FIZZBUZZ DIVISIBLE /15
# ELSE:INVALID

number = int(input("Enter the Number: "))
if number%15==0: # 
    print("FIZZBUZZ")
elif number%5==0:
    print("BUZZ")
elif number%3==0:
    print("FIZZ")
else:
    print("INVALID....")