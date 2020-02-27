from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Canvas Testing")

#root.peepeepoopoo; thanks sam

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainCanvas = Canvas(mainframe, width = 500, height = 500)
mainCanvas.pack()

mouseCoords = [0, 0, 0, 0]

def recordCoords(e):
    mouseCoords[0] = e.x
    mouseCoords[1] = e.y
    mouseCoords[2] = e.x_root
    mouseCoords[3] = e.y_root
    coordText.set("X: "+str(e.x)+"\nY: "+str(e.y)+"\nXr: "+str(e.x_root)+"\nYr: "+str(e.y_root))

root.bind("<B1-Motion>", recordCoords)

coordText = StringVar()
coordText.set("X: 0\nY: 0\nXr: 0\nYr: 0")

coordLabel = Label(mainframe, textvariable = coordText)
coordLabel.place(x=2, y=2, anchor=NW)

root.mainloop()