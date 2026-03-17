class Biriyani:

    name:str
    category:str
    price:int

def __init__(self,name,category,price):

# initialize attributes instance.
    self.name = name
    self.category = category
    self.price = price

# to initialize  attribute,instance variables.

def display(self):

    print(self.name,self.category,self.price)

Biriyani_instance1 = Biriyani("chicken_biriyani","non_veg",180)
Biriyani_instance1.display()
