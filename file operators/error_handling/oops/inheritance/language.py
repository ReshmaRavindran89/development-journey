# language :- (single inheritance)

class Language:

    def __init__(self,name):

        self.name = name

    def display(self):

        print(self.name)

class FrameWork(Language):

    def __init__(self,name,fname):
    
        super().__init__(name)
        
        self.fname = fname

    def display(self):

        super().display()

        print(self.fname)

FrameWork_instance = FrameWork("python","django")
FrameWork_instance.display()

