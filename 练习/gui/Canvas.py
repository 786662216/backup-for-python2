# coding:utf-8
'''
tkinter的基本用法
画布
'''
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('500x500')#大小

#创建画布控件
canvas = Canvas(window, #使画布位于window中
    bg='green', #设置画布背景色
    height=300, #设置画布高度
    width=300) #设置画布宽度

#设置image_file为tk中的PhotoImage变量，或者说是tk中的图片对象，这里似乎只能使用gif图片
image_file = PhotoImage(file='text.gif')

#在画布中显示图片
image = canvas.create_image(0,0, #图片坐标
    anchor='nw', #锚点位置
    image=image_file) #图片来源，必须是PhotoImage变量（tk中的图片对象）

x0,y0,x1,y1 = 0,0,50,50 #定义几个坐标变量方便后面使用，线段、圆形、扇形、矩形的大小都四个坐标确定

#在画布中显示线段
line = canvas.create_line(x0,y0,x1,y1)

#在画布中显示圆形，并用红色填充
oval = canvas.create_oval(x0+50,y0+50,x1+50,y1+50,fill='red')

#在画布中显示扇形
arc = canvas.create_arc(x0+100,y0+100,x1+100,y1+100,
    start=0, #设置扇形起点角度
    extent=180) #设置扇形终点角度

#在画布中显示矩形
rect = canvas.create_rectangle(x0+200,y0+200,x1+200,y1+200)

canvas.pack() #设置画布位置





window.mainloop()