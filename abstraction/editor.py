from abc import ABC,abstractmethod

class Editor:

    @abstractmethod
    def open(self):pass

    @abstractmethod
    def execute(self):pass

    @abstractmethod
    def debug(self):pass

class Vscode(Editor):

    def open(self):
        
        print("vscode opening")

    def execute(self):
        print("vscode execution")

    def debug(self):
        
        print("vscode debugging")

vscode_instance = Vscode()

vscode_instance.open()
vscode_instance.execute()
vscode_instance.debug()
