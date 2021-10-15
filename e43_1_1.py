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
        #没有在方法里引入他类作为参数
        #而是在类中引入属性，属性实参为他类的实例
        #好处，类内可能有很多方法，类属性中引入，则类内其他方法也能用
        current_room = 'rooma'
        while current_room != 'roomc':
            current_room = self.choose.chooseing()
               
            print("!")
        print("I'm in roomc now.")


choose = Chooser()
game = Engine(choose)
#y=f(x),x要可变
#则x是另一个类Choose的实例，
#x可使用Choose类的方法来改变返回的值
# ，x=g(z)
game.play()