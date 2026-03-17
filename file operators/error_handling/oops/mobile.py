
class Mobile:

    def __init__(self,image,name,price,rating):
        
        self.image = image
        self.name = name
        self.price = price
        self.rating =rating

    def display(self):

        print(self.image,self.name,self.price,self.rating)

Mobile_instance1 = Mobile("iphone.png","iphone16",120000,4.9)
Mobile_instance1.display()
