# coding:utf-8
'''
tkinter的基本用法
多选框
'''
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('500x500')#大小


label = Label(window,
              text='',
              bg='blue',
              width=30)
label.pack()

def print_choose():
    if(var1.get() == 1) & (var2.get() == 0):
        label.config(text='you have choose only A')
    elif(var1.get() == 0) & (var2.get() == 1):
        label.config(text='you have choose only B')
    elif(var1.get() == 0) & (var2.get() == 0):
        label.config(text='you have choose nothing')
    else:
        label.config(text='you have choose both A and B')


var1 = IntVar()
var2 = IntVar()

#创建两个复选框控件
c1 = Checkbutton(window, #使复选框位于window中
    text='选项A', #设置复选框文字
    variable=var1, #设置关联变量为var1,当c1被选中时，var1等于c1的value
    onvalue=1, #选中时c1的value为1
    offvalue=0, #未选中时c1的value为0
    command=print_choose)
c1.pack()
c2 = Checkbutton(window,text='选项B',variable=var2,onvalue=1,offvalue=0,command=print_choose)
c2.pack()


window.mainloop()