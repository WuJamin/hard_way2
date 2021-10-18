class Chooser():
    def choosing(self):
        val = input("Type a,b,c>  ")
        if val == 'a':
            return 'a'

        elif val == 'b':
            return 'b'

        elif val == 'c':
            return 'c'


class Engine():
    def __init__(self, choose):
        self.choose = choose

    def play(self):
        current_room = 'a'
        while current_room != 'c':
            print(f'in {current_room} now')
            current_room = choose.choosing()


choose = Chooser()
game = Engine(choose)
game.play()
