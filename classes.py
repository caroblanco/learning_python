class Point:
    def move(self):
        print('Move')

    def draw(self):
        print("Draw")


point1= Point()
point1.draw()
point1.move()
point1.x = 10
point1.y = 20
#x and y are attributes of point1

#CONTRUCTORS => function that gets called when we create an object
class Point:
    def __init__(self,x,y): #we initialize
        self.x = x
        self.y = y

    def move(self):
        print('Move')

    def draw(self):
        print("Draw")


point = Point(10,20)

#INHERITANCE
class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("woof")


class Cat(Mammal):
    pass        #no hace nada, pero las clases no pueden estar vacias


