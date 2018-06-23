# coding:utf-8
'''
tkinter的基本用法
单选控件
'''
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('800x800')#大小

var = StringVar()

label = Label(window,
              text='',
              width=20,
              bg='yellow')
label.pack()

#设置lable的text值
def print_choose():
    label.config(text = 'you have choose ' + var.get())



#创建一组单选框控件
r1 = Radiobutton(window, #使单选框控件位于window中
    text='选项A', #设置单选框文字
    variable=var, #将这组单选框与变量var关联，用var表示当前的选择状态
    value='A',
    command=print_choose) #设置单选框的value
r1.pack()
r2 = Radiobutton(window,text='选项B',variable=var,value='B',command=print_choose)
r2.pack()
r3 = Radiobutton(window,text='选项C',variable=var,value='C',command=print_choose)
r3.pack()
#r1、r2、r3都与变量var关联（var必须为全局变量），说明它们构成一组单选框，且var表示当前选中状态。
#当选中r1时，变量var被赋值为r1的value，此时value='A'的单选框被选中。由于r2、r3的value不是'A'，因此r2、r3变为未选中状态。
#如果r1、r2的value相同，比如都为'A'，当选中r1时，r2同时被选中，r3变为未选中状态。







window.mainloop()#不断的刷新窗口，类似于服务器的无限循环