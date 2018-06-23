# coding:utf-8
# 一个计算理财收益的小工具

from Tkinter import *
import tkMessageBox
import string

m = tkMessageBox

window = Tk()#传建一个顶级窗口
window.title('佘氏理财beta1.0')#标题

#图标
img = PhotoImage(file='./title.gif')
window.tk.call('wm', 'iconphoto', window._w, img)

window.geometry('400x400')#大小
screenwidth = window.winfo_screenwidth() #获取屏幕宽度
screenheight = window.winfo_screenheight() #获取屏幕高度

#使其出现在屏幕中央
window.geometry('%dx%d+%d+%d' % (400,400,(screenwidth-400)/2-10,(screenheight-400)/2-40))
window.resizable(False,False)#禁止调整大小

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()

#验证输入
def test(param):
    if len(param) == 0:
        m.showinfo(title='输入有误',message='输入不能为空')
        return ''
    for i in string.punctuation.replace('.','') + string.letters:
        if i in param:
            m.showinfo(title='输入有误', message='只能输入数字和小数点')
            return ''

    return float(param)
#计算收益
def cal():
    rate = test(e1.get()) / 100#年化收利率
    days =  test(e2.get())#期限
    capital =  test(e3.get())#本金
    pre_capital = capital
    years =  test(e4.get())#参投年数

    times = int((years * 365) / days)#参投次数
    var3.set(times)

    if (var1.get() == 'A'):
        for i in range(times):
            capital = (capital * rate) * (days / 365) + capital
            print capital
        result = capital
    else:
        result = capital * rate * times + capital
    var2.set(round(result,2))
    var4.set(round(result - pre_capital,2))

#清空输入
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


l1 = Label(window,text='年化收利率（%）：')
l1.place(x=100,y=30)
l2 = Label(window,text='期限（天）：')
l2.place(x=100,y=60)
l3 = Label(window,text='本金：')
l3.place(x=100,y=90)
l4 = Label(window,text='参投年数:')
l4.place(x=100,y=120)
l5 = Label(window,text='是否利滚利：')
l5.place(x=100,y=150)
r1 = Radiobutton(window,text='是',value='A',variable=var1)
r1.place(x=200,y=150)
r2 = Radiobutton(window,text='否',value='B',variable=var1)
r2.place(x=250,y=150)

e1 = Entry(window,text='rate')
e1.place(x=200,y=30)
e2 = Entry(window)
e2.place(x=200,y=60)
e3 = Entry(window)
e3.place(x=200,y=90)
e4 = Entry(window)
e4.place(x=200,y=120)

b1 = Button(window,text='计算收益',command=cal)
b1.place(x=180,y=180)
b1 = Button(window,text='清空',command=clear)
b1.place(x=280,y=180)

l5 = Label(window,text='参投次数：')
l5.place(x=100,y=220)
l6 = Label(window,textvariable=var3,bg='yellow',width=20)
l6.place(x=200,y=220)

l7 = Label(window,text='收益：')
l7.place(x=100,y=260)
l8 = Label(window,textvariable=var4,bg='red',width=20)
l8.place(x=200,y=260)

l7 = Label(window,text='收益+本金：')
l7.place(x=100,y=300)
l8 = Label(window,textvariable=var2,bg='green',width=20)
l8.place(x=200,y=300)

window.mainloop()