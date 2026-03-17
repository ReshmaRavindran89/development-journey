
# Single Inheritance:-

class Parent:

    def house(self):

        print("parent class house method")

class Child(Parent): # child is parent(child inherits parent methods & attributes)

    def moblie(self):

        print("child class mobile method")

child_instance = Child()
child_instance.moblie()
child_instance.house()
