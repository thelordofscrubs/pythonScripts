from tkinter import *
from tkinter import ttk
import math
import time

phyObCount = 0

class clickEvent:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time

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
        if m == 0:
            return [0,0]
        return [listin[0]/m, listin[1]/m]

    def returnMagnitude(self, listin):
        return math.sqrt(self.sqr(listin[0])+self.sqr(listin[1]))

    def sqr(self, x):
        return math.pow(x, 2)

    def add(self, v):
        self.x += v.x
        self.y += v.y
        self.Conf()

    def returnAdd(self, v):
        return Vector2(self.x+v.x, self.y+v.y)

    def mult(self, v):
        self.x *= v.x
        self.y *= v.y
        self.Conf()

    def returnMult(self, v):
        return Vector2(self.x*v.x, self.y*v.y)
    
    def returnPerp(self, reversedDir = "y"):
        if reversedDir == "y":
            return Vector2(-self.y, self.x)
        if reversedDir == "x":
            return Vector2(self.y, -self.x)
    
    def returnRev(self):
        return Vector2(-self.x, -self.y)
    
    def __add__(self, nv):
        return Vector2(self.x+nv.x,self.y+nv.y)
    
    def __mul__(self, nv):
        if type(nv) == int:
            return Vector2(self.x*nv, self.y*nv)
        else:
            return Vector2(self.x*nv.x,self.y*nv.y)
    
    def __sub__(self, nv):
        return Vector2(self.x-nv.x,self.y-nv.y)

class PhysicsObject:
    maxVel = 300.0

    def __init__(self, x = 10, y = 10, m = 1, p = False, velx = 0.0, vely = 0.0):
        global phyObCount
        self.pos = Vector2(x,y)
        self.m = m
        self.vel = Vector2(velx,vely)
        self.acc = Vector2(0,9)
        self.p = p
        self.id = phyObCount
        phyObCount+=1

    def applyVel(self, t):
        if self.p:
            return
        self.pos += self.vel * Vector2(t,t)
        global looping
        global canv
        if looping:
            if self.pos.x > canv.winfo_width():
                self.pos.x -= canv.winfo_width()
            if self.pos.x < 0:
                self.pos.x += canv.winfo_width()
            if self.pos.y > canv.winfo_height():
                self.pos.y -= canv.winfo_height()
            if self.pos.y < 0:
                self.pos.y += canv.winfo_height()

    def applyAcc(self, t):
        self.vel.x += self.acc.x*t
        if self.vel.x > self.maxVel:
            self.vel.x = self.maxVel
        if self.vel.x < -self.maxVel:
            self.vel.x = -self.maxVel
        self.vel.y += self.acc.y*t
        if self.vel.y > self.maxVel:
            self.vel.y = self.maxVel
        if self.vel.y < -self.maxVel:
            self.vel.y = -self.maxVel
    
    def __str__(self):
        return "Physics object id {5} at {0}, {1} with mass {2}, and vel {3}, {4}".format(round(self.pos.x,1), round(self.pos.y,1), self.m, round(self.vel.x,1), round(self.vel.y,1), self.id)

class Box(PhysicsObject):
    def __init__(self, x, y, size, canvas, m = 1, p = False, velx = 0.0, vely = 0.0):
        global phyObCount
        self.canvas = canvas
        super().__init__(x,y,m,p,velx,vely)
        self.size = size
        self.x1 = x+size
        self.y1 = y+size
        self.center = Vector2(x+(size/2),y+(size/2))
        self.id = phyObCount
        phyObCount+=1
        self.cr = canvas.create_rectangle(x,y,self.x1,self.y1, fill= rectColor, activefill = activeRectColor)

    def updateDisplay(self):
        self.canvas.coords(self.cr,self.pos.x,self.pos.y, self.pos.x+self.size, self.pos.y+self.size)

class POConnector:
    def __init__(self,o,o1,canvas):
        self.c1 = o.center
        self.o = o
        self.c2 = o1.center
        self.o1 = o1
        self.canvas = canvas
        self.v = c2-c1
        self.cr = canvas.create_line(self.c1.x,self.c1.y,self.c2.x,self.c2.y)

    def updateDisplay(self):
        self.canvas.coords(self.cr,self.c1.x,self.c1.y,self.c2.x,self.c2.y)

root = Tk()
root.title("Canvas Testing")

#root.peepeepoopoo; thanks sam

mainframe = ttk.Frame(root)
mainframe.pack()

canv = Canvas(mainframe, width = 750, height = 750)
canv.pack()

mouseCoords = [0, 0]

def recordCoords(e):
    mouseCoords[0] = e.x
    mouseCoords[1] = e.y
    coordText.set("X: "+str(e.x)+"\nY: "+str(e.y))

root.bind("<B1-Motion>", recordCoords)

clickLog = [clickEvent(0,0,0)]

def recordClicks(e):
    clickLog.append(clickEvent(e.x,e.y,0))
    if len(clickLog) >= 5:
        clickLog.pop(0)
    coordText.set("X: "+str(e.x)+"\nY: "+str(e.y))

root.bind("<1>", recordClicks)
root.bind("<1>", recordCoords)

coordText = StringVar()
coordText.set("X: 0\nY: 0")

coordLabel = Label(mainframe, textvariable = coordText)
coordLabel.place(x=2, y=2, anchor=NW)

rectColor = "#B36090"
activeRectColor = "#C9A4B5"

poText = StringVar()
poText.set("initialPO")
poLabel = Label(mainframe, textvariable = poText)
poLabel.place(x = 2, y = canv.winfo_height() - 10, anchor=SW)
poIndex = 0

def showPO(e):
    global poIndex
    poIndex += 1
    if poIndex > len(poList)-1:
        poIndex = 0
    #if poIndex == -1:
    #    poIndex = len(poList)-1

root.bind("s", showPO)

#canv.create_line(50,50,100,100)
#canv.create_rectangle(90,90,110,110, fill= rectColor, activefill = activeRectColor)

loopV = True

def stopLoop(e):
    loopV = False
    root.destroy()

root.bind("<Escape>", stopLoop)

firstPass = True
poList = []
timer = time.time()
looping = True


def physicsStep():
    global timer
    nt = time.time()
    for po in poList:
        po.applyAcc(nt-timer)
        po.applyVel(nt-timer)
        po.updateDisplay()
    timer = nt

def updateRoot():
    global poList
    physicsStep()
    #if showPOData:
    poText.set(str(poList[poIndex]))
    root.update()
    root.update_idletasks()

root.update()
root.update_idletasks()
canvasCenter = [canv.winfo_width()/2, canv.winfo_height()/2]
poList.append(Box(canvasCenter[0]-15, canvasCenter[1]-15, 30, canv))
poList.append(Box(360,400,30,canv))
poLabel.place(x = 2, y = canv.winfo_height() - 10, anchor=SW)

while loopV:
    updateRoot()
    pass