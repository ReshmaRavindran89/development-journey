
# create a function smart_sub with 2 parameter n1,n2
# return subtraction result as n1-n2 if n1>n2 else return n2-n1


def smart_sub(n1, n2):
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1

print(smart_sub(10, 20)) # Output: 10

