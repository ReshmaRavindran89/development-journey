
# def append(self,object) add object end of the list.

colors = ["red","green","blue"]
print(colors)

# object entering end of the list.

colors.append("black")
print(colors)

# def insert(self,object) specified new element  inserted in the list.

colors = ["red","black","blue"]
colors.insert(2,"yellow")
print(colors)        

# def pop(self,index=-1) remove and return specified element at index.

colors = ["red","green","blue"]
colors.pop(2)
print(colors)

# def remove(self,object) remove first ocurance of object.

colors = ["red","green","blue"]
colors.remove("green")
print(colors)

# def count(self,object) frequency of object in this list.

colors = ["red","green","blue","orange","red","red"]
print(colors.count("red"))
