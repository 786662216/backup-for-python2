# coding:utf-8
'''
tkinter的基本用法
框架可以对窗口中的各个控件进行布局，使窗口更加整齐美观，和html中的div标签有类似之处。
'''
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('500x500')#大小

l1 = Label(window,text='上标签').pack()

fm = Frame(window) #在window中创建框架fm
fm.pack()
fm_left = Frame(fm) #在fm中创建框架fm_left
fm_left.pack(side='left') #将fm_left放在fm的左侧
fm_right = Frame(fm) #在fm中创建框架fm_right
fm_right.pack(side='right') #将fm_right放在fm右侧

l2 = Label(fm_left,text='左1标签').pack()
l3 = Label(fm_left,text='左2标签').pack()
l4 = Label(fm_right,text='右标签').pack()




window.mainloop()