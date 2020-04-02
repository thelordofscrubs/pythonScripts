from tkinter import *
from tkinter import ttk
import math


root = Tk()
root.title("Canvas Testing")
loopUpdate = True


mainframe = ttk.Frame(root)
mainframe.pack()

canv = Canvas(mainframe, width = 750, height = 750)
canv.pack()

canv.create_line(50,700,700,700)
canv.create_line(50,700,50,50)

def grabDimensions(length):
    root = math.sqrt(length)
    r = math.ceil(root)
    l = math.floor(length/r)
    r = math.ceil(length/l)
    succsess = False
    while (abs(r-root) <= .01*length):
        if (l*r == length):
            succsess = True
            break
        l = math.floor(length/r)
        r = math.ceil(length/l)
    if succsess:
        atd = [r,l]
    else:
        atd = [math.ceil(root),math.ceil(root)]
    return atd

results = []
biggestX = 1
biggestY = 1

for x in range(1,500):
    results.append(grabDimensions(x))
    if results[-1][0] > biggestX:
        biggestX = results[-1][0]
    if results[-1][1] > biggestY:
        biggestY = results[-1][1]

for x in range(1,7):
    canv.create_line(50+x*100, 690, 50+x*100, 710)

for x in range(1,7):
    canv.create_line(40, x*100, 60, x*100)

screenCords = [0,0]
scalingX = 600/biggestX
scalingY = 600/biggestY

for x in range(6):
    canv.create_text(650-x*100,720,text = str(math.floor(biggestX/(x+1))))

for x in range(6):
    canv.create_text(30,100+x*100,text = str(math.floor(biggestY/(x+1))))

def placeDot(cord, t):
    spaces = cord[0]*cord[1]
    cord[0] *= scalingX
    cord[1] *= scalingY
    screenCords[0] = cord[0] + 50
    screenCords[1] = 700 - cord[1]
    canv.create_oval(screenCords[0]-1,screenCords[1]-1,screenCords[0]+1,screenCords[1]+1, fill = "#000000")
    canv.create_text(screenCords[0], screenCords[1]-10, font = "Arial 6", text = str(spaces-t))
    print("index "+str(t)+" has dimensions "+str(cord[0]/scalingX)+", "+str(cord[1]/scalingY)+" and has "+str(spaces-t)+" wasted spaces")

#placeDot([200,200], 5)

for r in range(0,len(results)):
    placeDot(results[r],r)
    #print(str(results[r]))

#canv.create_oval(100,100,102,102, fill = "#000000")

def updateRoot():
    root.update()
    root.update_idletasks()


while loopUpdate:
    updateRoot()
    pass