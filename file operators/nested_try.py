
lst = [10,11,12,13,14]

index = int(input("enter index"))

try:

    print(lst[index])

except Exception as e:

    index = int(input("enter index"))

    print(lst[index])

finally:
    
    print("file operation.....")
    print("db.....,commit")




