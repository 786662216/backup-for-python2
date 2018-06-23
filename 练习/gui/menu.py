# coding:utf-8
'''
tkinter的基本用法
画布
'''
from Tkinter import *

window = Tk()#传建一个顶级窗口
window.title('window')#标题
window.geometry('500x500')#大小

l = Label(window,text='',bg='yellow',width=35)
l.pack()

#定义菜单选项功能函数
def new_file():
    l.config(text='you have enter command: 新建文件')
def open_file():
    l.config(text='you have enter command: 打开文件')
def copy():
    l.config(text='you have enter command: 复制')
def paste():
    l.config(text='you have enter command: 粘贴')
def find():
    l.config(text='you have enter command: 查找')
def save_as_pdf():
    l.config(text='you have enter command: 另存为pdf')
def save_as_word():
    l.config(text='you have enter command: 另存为word')
def save_as_html():
    l.config(text='you have enter command: 另存为html')


menubar = Menu(window) #创建菜单栏menubar并使其位于window中

filemenu = Menu(menubar, #创建下拉菜单filemenun并使其位于菜单栏menubar中
    tearoff=0) #tearoff为1表示该菜单是可以独立出来的，为0表示不能独立出来

menubar.add_cascade(label='文件', #设置下拉菜单名称
    menu=filemenu) #将下拉菜单filemenu添加进菜单栏

filemenu.add_command(label='新建文件', #设置下拉菜单第一项名称
    command=new_file) #设置下拉菜单第一项功能

filemenu.add_command(label='打开文件', #设置下拉菜单第二项名称
    command=open_file) #设置下拉菜单第二项功能

filemenu.add_separator() #在下拉菜单中添加分隔线

filemenu.add_command(label='退出程序', #设置下拉菜单第三项名称
    command=window.quit) #第三项功能为关闭window

#用同样的方法创建第二个下拉菜单editmenu并设置各项名称、功能
editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='编辑', menu=editmenu)
editmenu.add_command(label='复制',command=copy)
editmenu.add_command(label='粘贴',command=paste)
editmenu.add_separator()
editmenu.add_command(label='查找',command=find)

#用同样的方法在下拉菜单filemenu中创建二级菜单secmenu并设置名称、功能
secmenu = Menu(filemenu,tearoff=0)
filemenu.add_cascade(label='另存为',menu=secmenu)
secmenu.add_command(label='pdf',command=save_as_pdf)
secmenu.add_command(label='word',command=save_as_word)
secmenu.add_command(label='html',command=save_as_html)

window.config(menu=menubar) #将自定义的菜单栏menubar设为window的菜单栏


window.mainloop()