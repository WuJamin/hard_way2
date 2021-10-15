class Engine():
    def __init__(self, choose):
        self.choose = choose

    def play(self):
        current_room = 'a'
        while current_room != 'c':
            current_room = self.choose.chooseing()
            if current_room == 'c':
                print("Good, You're in room C now.")
            else:
                print(f"You're in room{current_room} now.")


class Chooser():
    def chooseing(self):
        val = input("Enter your choose(a,b,c)\n> ")
        if val == 'a':
            return 'a'
        elif val == 'b':
            return 'b'
        elif val == 'c':
            return 'c'
        else:
            pass


choose = Chooser()
game = Engine(choose)
game.play()


