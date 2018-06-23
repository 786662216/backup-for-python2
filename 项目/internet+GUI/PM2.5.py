#-*-coding:utf-8-*-
import tkinter as tk
from tkinter import messagebox

pm2p5 = 233
m = messagebox

window = tk.Tk()
window.title(u'PM2.5预测系统')
window.geometry('550x450')
screenwidth = window.winfo_screenwidth() #获取屏幕宽度
screenheight = window.winfo_screenheight() #获取屏幕高度
window.geometry('%dx%d+%d+%d' % (550,450,(screenwidth-550)/2-10,(screenheight-450)/2-40))

#可视化界面
def Visualizing():
    console = tk.Toplevel(window)
    console.title(u'可视化演示')
    console.geometry('500x500')
    l1 = tk.Label(console, text=u'这里应该有图表或者代码')
    l1.pack()

def spider():
    var.set(u'正在爬取数据......')
    pass#此处正在爬取数据
    m.showinfo(title=u'提示', message=u'已经完成爬取！')
    var.set(u'已经完成爬取')

def preprocessing():
    var.set(u'正在进行预处理......')
    pass#此处进行预处理
    m.showinfo(title=u'提示', message=u'预处理已经完成！')
    var.set(u'预处理已经完成')

def analysis():
    var.set(u'正在进行相关性分析......')
    pass#此处进行相关性分析
    m.showinfo(title=u'提示', message=u'相关性分析已经完成！')
    var.set(u'相关性分析已经完成！')

#选测城市
def city():
    global var
    var = tk.StringVar()
    city = tk.Toplevel(window)
    city.title(u'请选择城市')
    city.geometry('250x400')

    BB = tk.Button(city, text=U'西安',width=15,
    height=2 ,command=console)
    BB.place(x=75, y=35)

    BB = tk.Button(city, text=U'上海',width=15,
    height=2)#,command=console)
    BB.place(x=75, y=90)

    BB = tk.Button(city, text=U'北京',width=15,
    height=2)#,command=console)
    BB.place(x=75, y=145)

    BB = tk.Button(city, text=U'郑州',width=15,
    height=2)#,command=console)
    BB.place(x=75, y=195)

    BB = tk.Button(city, text=U'石家庄',width=15,
    height=2)#,command=console)
    BB.place(x=75, y=245)

    BB = tk.Button(city, text=U'杭州',width=15,
    height=2)#,command=console)
    BB.place(x=75, y=300)

#控制台界面
def console():
    global var
    var = tk.StringVar()
    console = tk.Toplevel(window)
    console.title(u'控制台')
    console.geometry('250x400')

    l1 = tk.Label(console,
                  textvariable = var,
                  bg='yellow',
                  font=('Arial', 12),
                  width=25,
                  height=4)
    l1.pack()

    BB = tk.Button(console, text=U'爬取数据',width=15,
    height=2 ,command=spider)
    BB.place(x=75, y=90)

    BB = tk.Button(console, text=U'预处理',width=15,
    height=2,command=preprocessing)
    BB.place(x=75, y=145)

    BB = tk.Button(console, text=U'相关性分析',width=15,
    height=2,command=analysis)
    BB.place(x=75, y=195)

    BB = tk.Button(console, text=U'可视化',width=15,
    height=2,command=Visualizing)
    BB.place(x=75, y=245)


#判断pm2.5
def pm(value):
    if value > 350 or value == 350:
        return u'报表!'
    elif value < 350 and (value > 250 or value == 250):
        return u'严重污染'
    elif value < 250 and (value > 150 or value == 150):
        return u'重度污染'
    elif value < 150 and (value > 115 or value == 115):
        return u'中度污染'
    elif value < 115 and (value > 75 or value == 75):
        return u'轻度污染'
    elif value < 75 and (value > 35 or value == 35):
        return u'良'
    elif value < 35 and (value > 0 or value == 0):
        return u'优'

#主界面
l1 = tk.Label(window,
    text=u'今日PM2.5：' + str(pm2p5)+ u'，' + pm(pm2p5),
    bg='yellow',
    font=('Arial',12),
    width=50,
    height=8)
l1.place(x=50,y=30)

l2 = tk.Label(window,
    text=u'今日天气：多云转晴\n'
         u'-20-38度',
    bg='yellow',
    font=('Arial',12),
    width=30,
    height=4)
l2.place(x=150,y=200)

b = tk.Button(window,
    text=u'选择城市',
    width=10,
    height=2,
    command=city)
b.place(x=240,y=330)

window.mainloop()