
# find duplicates without using any predefined methods:-

lst = [10,11,12,11,13,15,14,13]

#      10,11,11,12,13,13,14,15

#       0  1  2  3  4  5  6  7

#       p  n

lst.sort()

for prev in range(0,len(lst)-1):

    next = prev + 1
    difference = lst[next] - lst[prev]

    if difference ==0:
        print(lst[prev])

"""
Using predefind method:-

"""

def find_duplicates(arr):
    arr.sort()

    for prev in range(0,len(arr)-1):

        next = prev + 1
        difference = arr[next] - arr[prev]

        if difference ==0:
            print(arr[prev])
            
find_duplicates([11,12,11,13,14,14])

