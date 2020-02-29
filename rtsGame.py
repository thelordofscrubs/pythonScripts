import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Conf()
    
    def Conf(self) :
        self.list = [self.x, self.y]
        self.unit = self.makeUnit(self.list)
        self.mag = self.returnMagnitude(self.list)

    def makeUnit(self, listin):
        m = self.returnMagnitude(listin)
        return [listin[0]/m, listin[1]/m]

    def returnMagnitude(self, listin):
        return math.sqrt(self.sqr(listin[0])+self.sqr(listin[1]))

    def sqr(self, x):
        return math.pow(x, 2)

    def add(self, v = Vector2(0,0)):
        self.x += v.x
        self.y += v.y
        self.Conf()

    def returnAdd(self, v = Vector2(0,0)):
        return Vector2(self.x+v.x, self.y+v.y)

    def mult(self, v):
        self.x *= v.x
        self.y *= v.y
        self.Conf()

    def returnMult(self, v):
        return Vector2(self.x*v.x, self.y*v.y) 