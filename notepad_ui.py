#UI Window

from tkinter import *

window = Tk()
# theLabel=Label(window, text="Please write something below")
# theLabel.pack()
# window.title("Test Window")

window.geometry("960x540")
topFrame=Frame(window)
topFrame.grid(row=0,column=0)


# bottomFrame=Frame(window)
# bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text="Save written",fg="green")
button1.grid(row=0,column=0)

window.mainloop()