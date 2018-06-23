# coding:utf-8
'''
tkinter的基本用法
输入框、文本框
'''
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('800x800')#大小




var1 = StringVar()#设置var1为tk中的StringVar变量
var1.set([11,22,33,44])

var2 = StringVar()#用来存放从列表中取出的内容


#列表框控件
listbox = Listbox(window,#放在window中
                  listvariable=var1)#内容为var1

#几种更改列表框的方法
list = [1,2,3,4]
for l in list:
    listbox.insert('end',l)#通过循环insert方法

listbox.insert(1,'first') #在列表框第1行插入'first'
listbox.insert(2,'second') #在列表框第2行插入'second'
listbox.delete(2) #将列表框第2行元素删除，下面的元素会依次填充上来

listbox.pack()


#选择列表框中的某行，点击按钮，该行内容便显示在一个标签上
def print_choose():
    value = listbox.get(listbox.curselection())
    var2.set(value)

button = Button(window,
                text='print',
                command=print_choose)
button.pack()

#var2取出来放到这个标签里
entry = Label(window,
              textvariable=var2,
              bg='green',
              width=15,
              height=1)
entry.pack()


window.mainloop()#不断的刷新窗口，类似于服务器的无限循环