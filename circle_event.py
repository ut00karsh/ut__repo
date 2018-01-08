from tkinter import *
import tkMessageBox
a=[]
b=[]
def callback():
    if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()
def f1(event):
	global a,b
	c.create_oval(event.x-10,event.y+10,event.x+10,event.y-10,tag="o")
	a.append(event.x-10)
	b.append(event.y+10)
	a.append(event.x+10)
	b.append(event.y-10)
	c.create_rectangle(min(a),max(b),max(a),min(b))
root=Tk()
top = Toplevel(root)
top.title("About this application...")

msg = Message(top, text="Welcome to the application")
msg.pack()

button = Button(top, text="Dismiss", command=top.destroy)
button.pack()
c=Canvas(root,width=500,height=500)
x=0,0,0,0
c.create_rectangle(x)
c.pack()
c.bind("<Button-1>",f1)
root.protocol("WM_DELETE_WINDOW", callback)




mainloop()