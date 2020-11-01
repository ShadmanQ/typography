#UI Window

from tkinter import *

def LeftClick(event):
    print("Save function")

def CanvasClick(event):
    print("Canvas clicked")
    canvas.create_rectangle(event.x,event.y,event.x+2,event.y+2,width=3)
    
window = Tk()
# theLabel=Label(window, text="Please write something below")
# theLabel.pack()
# window.title("Test Window")

#window.geometry("960x540")
topFrame=Frame(window)
topFrame.pack()


bottomFrame=Frame(window)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text="Save written",fg="green")
button1.bind("<Button-1>",LeftClick)
# # button1.grid(row=0,column=0)
button1.pack()

canvas = Canvas(bottomFrame,width=960,height=540,bg="old lace")
canvas.bind("<B1-Motion>",CanvasClick)
canvas.pack()
#canvas.grid(row=0,column=2)

window.mainloop()
