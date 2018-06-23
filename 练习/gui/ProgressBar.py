# coding:utf-8
from Tkinter import *

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())

tk = Tk()
tk.geometry('250x150')#顶层窗口的大小；注意x是小写

label = Label(tk,text='caonima',font='Helvetica -12 bold')
label.pack(fill=Y,expand=1)

scale = Scale(tk,from_=50,to=200,orient=HORIZONTAL,command=resize)
scale.set(110)
scale.pack(fill=X,expand=1)

quit = Button(tk,text='quit',command=tk.quit,activeforeground='white',activebackground='red')
quit.pack()

mainloop()
