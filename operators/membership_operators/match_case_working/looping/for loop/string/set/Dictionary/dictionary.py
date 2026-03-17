
"""
Dictionary:-

dictionary = {key:value,key:value,......}
Accessing value using key.

"""
notebook = {"brand":"classmate","price":40,"line":"double line"}
print(notebook["brand"])

# Update value:-
# Update lines as single line.

notebook["line"] = "single line"
print(notebook)

# create a dictionary of product with attribute

#  id , title ,price ,avl_qty

bag = {"id":87,"title":"skybags","price":2000,"avl_qty":10}

print(bag)

# update => avl_qty into 20.

bag = {"id":87,"title":"skybags","price":2000,"avl_qty":10}
bag["avl_qty"]+=10

print(bag)

# Add code:skul2

bag["code"] = "skul2"
print(bag)

# check key is exist or not.

if "offer" in bag:

    print("Exist")

else:
    
    print("Not exist")
