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

class PhysicsObject:
    maxVel = 300.0

    def __init__(self, x = 10, y = 10, m = 1, p = False, velx = 0.0, vely = 0.0):
        global phyObCount
        self.x = x
        self.y = y
        self.m = m
        self.velx = velx
        self.vely = vely
        self.accx = 0.0
        self.accy = .5
        self.p = p
        self.id = phyObCount
        phyObCount+=1

    def applyVel(self, t):
        self.x += self.velx*t
        self.y += self.vely*t
        global looping
        global canv
        if looping:
            if self.x > canv.winfo_width():
                self.x -= canv.winfo_width()
            if self.x < 0:
                self.x += canv.winfo_width()
            if self.y > canv.winfo_height():
                self.y -= canv.winfo_height()
            if self.y < 0:
                self.y += canv.winfo_height()

    def applyAcc(self, t):
        self.velx += self.accx*t
        if self.velx > self.maxVel:
            self.velx = self.maxVel
        if self.velx < -self.maxVel:
            self.velx = -self.maxVel
        self.vely += self.accy*t
        if self.vely > self.maxVel:
            self.vely = self.maxVel
        if self.vely < -self.maxVel:
            self.vely = -self.maxVel
    
    def __str__(self):
        return "Physics object id {5} at {0}, {1} with mass {2}, and vel {3}, {4}".format(self.x, self.y, self.m, self.velx, self.vely, self.id)

class Box(PhysicsObject):
    def __init__(self, x, y, size, canvas, m = 1, p = False, velx = 0.0, vely = 0.0):
        global phyObCount
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.x1 = x+size
        self.y1 = y+size
        self.m = m
        self.p = p
        self.velx = velx
        self.vely = vely
        self.accx = 0.0
        self.accy = 9.8
        self.p = p
        self.id = phyObCount
        phyObCount+=1
        self.cr = canvas.create_rectangle(self.x,self.y,self.x1,self.y1, fill= rectColor, activefill = activeRectColor)

    def updateDisplay(self):
        self.canvas.coords(self.cr,self.x,self.y, self.x+self.size, self.y+self.size)

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
poText.set("")

def showPO(e):
    poLabel = Label(mainframe, textvariable = poText)
    poLabel.place(x = 2, y = canv.winfo_height() - 10, anchor=SW)
    poText.set(str(poList[0]))

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
    global firstPass
    global poList
    physicsStep()
    root.update()
    root.update_idletasks()
    if firstPass:
        canvasCenter = [canv.winfo_width()/2, canv.winfo_height()/2]
        poList.append(Box(canvasCenter[0]-15, canvasCenter[1]-15, 30, canv))
        firstPass = False

while loopV:
    updateRoot()
    pass