
def count_of_odd(*args:tuple):

    odd = [num for num in args if num%2!=0]

    return len(odd)

print(count_of_odd(10,11,12,13))
print(count_of_odd(10,11,12,13,14,15,16))


