# coding:utf-8
'''
tkinter的基本用法
输入框、文本框
'''
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('800x800')#大小

var = StringVar()#设置var为tk中的StringVar变量
var.set('my window')

#输入框控件
entry = Entry(window, #使输入框位于window中
    show='*') #设置输入内容不可见，如果show=None则为可见，默认值为None
entry.pack() #设置输入框位置

#在输入框中输入文字，点击按钮，文字插入到文本框中。且有两种插入方式，一种是将文字插入到光标所在位置，另一种是将文字插入到文本框中文字的结尾。
def insert_point():
    var = entry.get() #获得输入框中的文字
    text.insert('insert',var) #将变量var插入文本框t中，'insert'表示从光标处插入
def insert_end():
    var = entry.get()
    text.insert('end',var) #'end'表示从结尾处插入

button2 = Button(window,
                text='insert',
                width=15,
                height=2,
                command=insert_point#点击时回调hit函数
                )
button2.pack()
button3 = Button(window,
                text='end',
                width=15,
                height=2,
                command=insert_end#点击时回调hit函数
                )
button3.pack()

#文本框控件
text = Text(window, #使文本框位于window中
    height=2) #设置文本框高度
text.pack() #设置文本框位置




window.mainloop()#不断的刷新窗口，类似于服务器的无限循环