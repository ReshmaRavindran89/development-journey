"""
sample input1:
    lst=[1,2,3,5]

    o/p => 4

"""

lst = [1,2,3,5]
length = len(lst)

for i in range(1,length+1):

    if i not in lst:
        print(i,"is missing")
        break

"""
sample input3:
    lst=[1,2,3,4,5]
    o/p=>6

"""
lst = [1,2,3,4,5]
length = len(lst)

for i in range(1,length+1):

    if i not in lst:
        print(i,"is missing")

        break
else:
    print(length+1,"is missing")


# Another method to find missing number #

lst = [1,2,4,5]
#      0 1 2 3
#      prev next

lst.sort()

prev = 0
next = prev + 1

while(prev<=len(lst)-2):
    difference = lst[next] - lst[prev]

    if difference!=1:
        print(lst[prev]+1 ,"is missing")

        break
    prev+=1          # here we are changing the place of previous.
    next = prev+1    # here we are changing the place of next.

    """
    Another method to find missing number using arr with while loop:-

    """
    
def missing_least_positve(arr):
    arr.sort()

    prev = 0
    next = prev + 1

    while(prev<=len(arr)-2):
        difference = arr[next] - arr[prev]

        if difference!=1:
            print(arr[prev]+1 ,"is missing")

        break
    prev+=1          
    next = prev+1
missing_least_positve([1,2,4])

"""
Another method to find missing number using arr with for loop:-

    lst=[1,2,3,4]
    o/p=>5

"""
lst =[1,2,3,4]
#     0 1 2 3 
#     p n

def missing_least_positive(arr):
    arr.sort()

    for prev in range(0,len(arr)-1):

        next = prev + 1

        difference = arr[next] - arr[prev]

        if difference!=1:
            print(arr[prev]+1 ,"is missing")

            break
    else:
        print(arr[-1]+1)   

missing_least_positive([1,2,3,4])
                      

