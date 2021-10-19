class Other():
    def override(self):
        print("other override")

    def implicit(self):
        print("other implicit")

    def altered(self):
        print("other altered")

class Child():
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("child override")

    def altered(self):
        print("child, before other altered")
        #super(Child, self).altered()
        self.other.altered()
        print("child, after ohter altered")

son = Child()

son.other.implicit()
son.implicit()
son.override()
son.altered()