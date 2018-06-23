# coding:utf-8
'''
tkinter的基本用法
弹出窗口
'''
import Tkinter as tk
import tkMessageBox

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

m = tkMessageBox

def info():
    m.showinfo(title='普通提示信息', message='请稍等，正在获取资源···')
def little_error():
    m.showwarning(title='错误提示信息',message='抱歉，本站没有该资源！')
def serious_error():
    m.showerror(title='严重错误提示信息',message='警告，您下载的文件可能含有木马程序！')
def upload():
    mb1 = m.askquestion(title='询问并返回yes/no',message='确定要上传资源吗？') #使用askquestion会得到一番返回值（yes 或 no）
    if mb1 == 'yes': #可以利用返回值进行其他操作
        m.showwarning(title='错误提示信息',message='非VIP用户禁止上传资源！')
def collect():
    mb2 = m.askyesno(title='询问并返回True/False',message='确定要收藏该资源吗？') #使用askyesno会得到一番返回值（True 或 False）
    if mb2: #可以利用返回值进行其他操作
        m.showinfo(title='普通提示信息',message='感谢您的收藏！')

b1 = tk.Button(window,text='下载视频“海贼王”',command=info,width=40).pack()
b2 = tk.Button(window,text='下载视频“楚门的世界”',command=little_error,width=40).pack()
b3 = tk.Button(window,text='下载视频“ちーちゃんと秘密のアルバイト”',command=serious_error,width=40).pack()
b4 = tk.Button(window,text='上传视频“权利的游戏 第八季”',command=upload,width=40).pack()
b5 = tk.Button(window,text='收藏视频“侏罗纪公园”',command=collect,width=40).pack()

window.mainloop()