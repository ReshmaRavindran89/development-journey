# display sum of odd numbers and even numbers upto limit 6

limit = int(input("Enter Limit: "))
i = 1
even_sum= 0
odd_sum = 0
while(i<=limit):
    if i%2==0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
    i = i+1
print("even sum",even_sum)
print("odd sum",odd_sum)
