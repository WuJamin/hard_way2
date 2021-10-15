class Rooma():
    pass


class Roomb():
    pass


class Roomc():
    pass


class Chooser():
    def chooseing(self):
        val = input("type a,b,c> ")
        if val == 'a':
            return 'rooma'
        elif val == 'b':
            return 'roomb'
        elif val == 'c':
            return 'roomc'
        else:
            pass


class Engine():

    def __init__(self, choose):
        self.choose = choose

    
    def play(self):
        current_room = 'rooma'
        while current_room != 'roomc':
            current_room = self.choose.chooseing()
               
            print("!")
        print("I'm in roomc now.")


choose = Chooser()
game = Engine(choose)
game.play()