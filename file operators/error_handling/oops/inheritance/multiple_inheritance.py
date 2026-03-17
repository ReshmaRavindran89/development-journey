
# Multiple Inheritance:-

class Father:

    def dancing_skill(self):

        print("Dancing skill")

class Mother:

    def singing_skill(self):

        print("singing skill")

class Child(Father,Mother):

    pass

child_instance = Child()
child_instance.dancing_skill()
child_instance.singing_skill()

