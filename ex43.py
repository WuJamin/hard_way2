from sys import exit
from random import randint
from textwrap import dedent

class Scene():
    
    def enter(self):
        print("This scene is not yet configued.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(): #引擎类，接受一个当前场景地图

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        """
        self是a_game实例，scene_map是形参，会被a_map实参代替，
        而a_map是Map的实例，有opening_scene()方法
        """
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mon would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The gothons of planet
        you're running down the central corridor to the wepons
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
            quick on the draw you yank out your blaster and fire
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
            Like a world,
            eats you.
            """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
            Lucy for you
            weapon armory door
            """))
            return 'laster_weapon_armory'

        else:
            print("does not compute!")
            return 'central_corridor' #怎么接收？


class LasterWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        You do a dive
        The code is 3 digits.
        """))

        code = f"{randint(1, 9)} {randint(1, 9)} {randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
            The lockbuzzes one last time
            in the right spot.
            """))
            return 'the_bridge'
    
        else:
            print(dedent("""
            The lock
            you dead.
            """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        You best
        set it off.
        """))
        
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
            In a panic
            goes off.
            """))
            return 'death'
        elif action == 'slowly place the bomb':
            print(dedent("""
            You point your blaster
            get off this tin can.
            """))
            return 'escape_pod'
        else:
            print("does not compute!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        You rush through
        which one do you take?
        """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
            You jump into
            jam jelly.
            """))
            return 'death'
        else:
            print(dedent("""
            You jump into
            you win.
            """))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! good job.")
        return 'finished'


class Map():
    #地图类，里面有场景字典，有个开始场景属性

    scenes = {
        'central_corridor': CentralCorridor(),
        'laster_weapon_armory': LasterWeaponArmory(),
        'the_birdge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name): 
        #方法，接收字符串场景名，返回对应场景类      
        val = Map.scenes.get(scene_name)
        return val
        '''
        Map()类有一个scenes属性
        scenes是一个字典，键是场景字符串，值是场景类
        Map()类中有next_scene方法，接受一个参数x，
        Map对象的scenes
        scenes是字典，再对字典使用get(x)方法，
        即返回键x，的值，此值是类。
        '''

    def opening_scene(self): 
        return self.next_scene(self.start_scene)
        '''
        方法，不接受参数（接收了实例的开始场景属性），返回场景类，
        岂不是和上面方法一样吗？
        只返回创建实例时，填的属性对应的场景。
        也就是说他只返回固定一个场景类
        ？？？和next_scene()构成递归？一个给递归，一个给基例？

        self.next_scene(self.start_scene)
        第一个self,代指实例，即后面新建的a_map
        next_scene(self.start_scene)
        中的self.start_scene是Map()类的start_scene属性
        '''


'''a_map = Map('central_corridor')
a_game = Engine(a_map) #Engine类接受一个“当前场景”属性，此处以a_map作为实参，而a_map实例有切换场景的函数。
a_game.play()'''



