# coding:utf-8
'''
tkinter的基本用法
滚动条
'''
#pack()
# pack()前面已经介绍过了，可以将side参数设为'top'、'left'、'right'、'bottom'分别将控件放在正上方、正左边、正右边、正下方，side的默认值为'top'。
# 此外，pack()还有expand、fill、padx、pady、ipadx、ipady等属性，这里不作详细介绍。
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('500x500')#大小


#grid()
#grid意为格子，grid()将控件放在一个一个的格子中，就像放在表格中一样，可以使用grid()对控件进行布局。
for i in range(4):
    for j in range(3):
        Label(window,text=123).grid(row=i,column=j)

#place()
#place()可以通过猫和坐标参数将控件放在窗口的某个点上，例如：
Label(window,text=123,bg='green',width=10).place(x=100,y=100,anchor='nw')

window.mainloop()












window.mainloop()
