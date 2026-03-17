"""
method over riding:-

child class redefines the method that is already defined in parent class.

"""

class Parent:

    def vechicle(self):

        print("Passion Pro")


class Child(Parent):

    def vechicle(self):

        print("Pulsar 250")

child_instance = Child()

child_instance.vechicle()
