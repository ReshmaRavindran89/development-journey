
# Multilevel Inheritance:-

class GrandParent:

    def properties(self):

        print("grandparent propreties")

class Parent(GrandParent):

    def house(self):

        print("parent house method")

class Child(Parent):

    pass

child_instance = Child()
child_instance.properties()
child_instance.house()


