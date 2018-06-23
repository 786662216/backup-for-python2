# coding:utf-8
'''
tkinter的基本用法
顶级窗口、按钮、标签
'''
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('800x800')#大小

var = StringVar()#设置var为tk中的StringVar变量
var.set('my window')


#标签控件
label = Label(window,#这个标签控件将放在window中
              #text='123',文本内容,字符串变量
              textvariable=var,#文本变量
              bg='green',#背景颜色
              font=('Arial',12),#字体及大小
              width=15,#宽度
              height=2)#高度
label.pack()#设置标签的位置，无参数将默认放置在正上方


#控制标签文字
on_hit = False #用来表示标签文字状态，False表示为空，True表示非空
def hit():
    global on_hit
    if on_hit == False:#如果标签文字为空
        var.set('my label')#将其设置为'my label'
        on_hit =True#更新标签文字状态
    else:#否则
        var.set('')#将其设置为空
        on_hit = False#更新标签文字状态


#按钮控件
button1 = Button(window,
                text='my button',
                width=15,
                height=2,
                command=hit#点击时回调hit函数
                )
button1.pack()

window.mainloop()


