#W.A.P to check the last two digit of a number is less than twenty

number = 125
last_two_digit= number % 100 # 125%100
is_last_two_less_twenty = last_two_digit > 20 
print(is_last_two_less_twenty)
