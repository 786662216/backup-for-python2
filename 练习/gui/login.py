# coding:utf8
from Tkinter import *

#顶级窗口初始化
window = Tk()
window.title('情非得已V2.0用户登录')
screenwidth = window.winfo_screenwidth() #获取屏幕宽度
screenheight = window.winfo_screenheight() #获取屏幕高度
#使其出现在屏幕中央
window.geometry('%dx%d+%d+%d' % (1000,400,(screenwidth-1000)/2-10,(screenheight-400)/2-40))
# window.geometry('1000x400')
window.resizable(False,False)#禁止调整大小


def login():
    pass
def regirst():
    console = Toplevel(window)  # 创建一个在window上的新窗口用于注册，由于主窗口window已经进行了mainloop，所以注册窗口不需要使用mainloop()
    console.title('注册窗口')
    console.geometry('400x250')

    new_name = StringVar()
    Label(console, text='用户名').place(x=100, y=30)
    entry_new_name = Entry(console, textvariable=new_name)
    entry_new_name.place(x=180, y=30)

    new_password = StringVar()
    Label(console, text='密码').place(x=100, y=70)
    entry_new_password = Entry(console, textvariable=new_password, show='*')
    entry_new_password.place(x=180, y=70)

    new_password_confirm = StringVar()
    Label(console, text='确认密码').place(x=100, y=110)
    entry_new_password_confirm = Entry(console, textvariable=new_password_confirm, show='*')
    entry_new_password_confirm.place(x=180, y=110)

    BB = Button(console, text='确认注册')
    BB.place(x=220, y=150)


#登录窗口图片
#创建画布控件
canvas = Canvas(window, #使画布位于window中
    bg='white', #设置画布背景色
    height=121, #设置画布高度
    width=740) #设置画布宽度
#设置image_file为tk中的PhotoImage变量，或者说是tk中的图片对象，这里似乎只能使用gif图片
image_file = PhotoImage(file='welcome.gif')
#在画布中显示图片
image = canvas.create_image(0,0, #图片坐标
    anchor='nw', #锚点位置
    image=image_file) #图片来源，必须是PhotoImage变量（tk中的图片对象）

canvas.pack()


#用户名、密码标签
Label(window,text='用户名：').place(anchor='nw',x=260,y=220)
Label(window,text='密码：').place(anchor='nw',x=260,y=300)

#用户名、密码输入标签
Entry(window).place(anchor='nw',x=320,y=220,width=400)
Entry(window,show='*').place(anchor='nw',x=320,y=300,width=400)

#登录注册按钮
Button(window,text='登录',width=10,height=1,command=login).place(x=360,y=350)
Button(window,text='注册',width=10,height=1,command=regirst).place(x=600,y=350)


window.mainloop()