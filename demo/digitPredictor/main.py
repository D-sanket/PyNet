from math import floor
from tkinter import *

canvas_width = 560
canvas_height = 560

px = None
py = None
lineSize = 40
blankArray = []

for i in range(28):
    t = []
    for j in range(28):
        t.append(0)
    blankArray.append(t)

drawingArray = blankArray

def paint(event):
    global px, py, lineSize
    if px is not None and py is not None:
        x, y = event.x, event.y
        appX, appY = floor(x/20), floor(y/20)
        drawingArray[appY][appX] = 1
        drawingArray[appY-1][appX] = 1
        drawingArray[appY+1][appX] = 1
        drawingArray[appY][appX-1] = 1
        drawingArray[appY][appX+1] = 1
        w.create_line(px, py, x, y, fill="#000000", width=lineSize)
        w.create_oval(x-lineSize/2, y-lineSize/2, x+lineSize/2, y+lineSize/2, fill="#000000")
        px, py = event.x, event.y
    else:
        px, py = event.x, event.y

def forgetLastPoint(event):
    global px, py
    px, py = None, None

def onDblClick(event):
    with open("img.txt", "w") as oFile:
        for lineArray in drawingArray:
            line = ''.join([str(x) for x in lineArray])
            oFile.write(line+"\n")


master = Tk()
master.title("Painting using Ovals")
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=YES, fill=BOTH)
w.bind("<B1-Motion>", paint)
w.bind("<ButtonRelease-1>", forgetLastPoint)
w.bind("<Double-Button-1>", onDblClick)

message = Label(master, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)

mainloop()
