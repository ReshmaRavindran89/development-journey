
# whether number is fibanocci or not.

def is_fibinocci_number(number):
 
    is_fibo =  False
    prev = 0 
    curr = 1
    next = prev + curr
    while(next<=number):
        next = prev + curr
        prev = curr
        curr = next

        if next == number:
            is_fibo =  True

            break

    return is_fibo
print(is_fibinocci_number(3))
print(is_fibinocci_number(5))
print(is_fibinocci_number(8))