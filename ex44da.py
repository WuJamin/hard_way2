class Parent():
    def override(self):
        print("parent override()")


class Child(Parent):
    
    def __init__(self, stuff):
        self.stuff = stuff
        #super(Child, self).__init__()

dad = Parent()
son = Child("name")

son.override()