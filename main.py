from tkinter import *
from time import *
from random import *

def create_circle(x, y, r,canvasName,color="red"): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,outline=color,fill="blue")


root = Tk()
root.title("CLOCK")
root.resizable(height=False,width=False)
canvas = Canvas(height=220,width=220,bg="pink")
canvas.pack()
circle = create_circle(110,110,100,canvas)
canvas.update()
# while 1:
#     time_str = strftime('%H:%M:%S:%p')
#     time_text = canvas.create_text(110,110,fill="red",font=("Times",30))
#     canvas.itemconfig(time_text,text=time_str)
#     canvas.update()
#     canvas.delete(time_text)
def clock():
    time_str = strftime('%H:%M:%S:%p')
    label = Label(canvas,text=time_str,font=("Times",30),bg="blue",fg="yellow")
    label.place(x=22,y=95)
    label.after(1000,clock)

clock()
root.mainloop()