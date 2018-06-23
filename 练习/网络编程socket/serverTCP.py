#coding:utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 2333
ADDRESS=(HOST,PORT)

server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print "waiting for connection······"
    client,addr = server.accept()
    #accept返回一个元组，包含一个新的socket对象和地址对
    print '···connected from:',addr

    while True:
        data = client.recv(1024)
        print data
        if not data:
            break
        client.send('[%s]  %s' % (ctime(),data))
        #send方法发送一个字符串对象
    client.close()

server.close()
