from tkinter import *
a=[]
b=[]
def f1(event):
	global a,b
	c.create_oval(event.x-10,event.y+10,event.x+10,event.y-10,tag="o")
	a.append(event.x-10)
	b.append(event.y+10)
	a.append(event.x+10)
	b.append(event.y-10)
	c.create_rectangle(min(a),max(b),max(a),min(b)


root=Tk()
c=Canvas(root,width=200,height,200)
x=0,0,0,0
c.create_rectangle(x)
c.pack()
c.bind("<Button-1>",f1)
mainloop()
