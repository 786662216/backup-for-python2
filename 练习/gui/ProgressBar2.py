# coding:utf-8
'''
tkinter的基本用法
滚动条
'''
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('500x500')#大小

lable = Label(window,
              bg='yellow',
              text='',
              width=20)
lable.pack()

def print_choose(v):
    lable.config(text='you have choose ' + v)

scale = Scale(window,
              label='my scale',  # 设置滑动条名称
              from_=0,  # 设置最小值
              to=10,  # 设置最大值
              orient=HORIZONTAL,  # 设置滑动条为横向
              length=200,  # 设置滑动条宽度为200像素
              showvalue=1,  # 将选中的值显示在滑块上面，如果为0则不显示
              tickinterval=2,  # 以2为间隔显示刻度
              resolution=0.1,  # 精确到0.1
              command=print_choose)  # 点击滑动条执行函数print_choose
scale.pack()

window.mainloop()