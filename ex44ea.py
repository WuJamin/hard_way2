class Parent():
    def do1(self):
        print("parent, doing")

    def do2(self):
        print("parent, do2")

class Son():
    def __init__(self):
        self.b = Parent()
    
    def c(self):
        self.b.do1()

son = Son()
son.b.do1()