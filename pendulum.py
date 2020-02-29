from tkinter import *
from tkinter import ttk
import math

class clickEvent:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time

root = Tk()
root.title("Canvas Testing")

#root.peepeepoopoo; thanks sam

mainframe = ttk.Frame(root)
mainframe.pack()

canv = Canvas(mainframe, width = 500, height = 500)
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

root.bind("<1>", recordClicks)
root.bind("<1>", recordCoords)

coordText = StringVar()
coordText.set("X: 0\nY: 0")

coordLabel = Label(mainframe, textvariable = coordText)
coordLabel.place(x=2, y=2, anchor=NW)

canv.create_line(50,50,100,100)
canv.create_rectangle(90,90,110,110, fill="#B36090")

loopV = True

def stopLoop(e):
    loopV = False

root.bind("<Escape>", stopLoop)

def updateRoot():
    root.update()
    root.update_idletasks()

while loopV:
    updateRoot()
    pass