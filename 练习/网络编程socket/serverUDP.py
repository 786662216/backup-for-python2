#coding:utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 23333
ADDRESS = (HOST,PORT)

server = socket(AF_INET,SOCK_DGRAM)
server.bind(ADDRESS)

while True:
    print 'waiting......'
    data,addr = server.recvfrom(1024)
    DATA = (data,addr)
    print 'recv: %s' % str(DATA)
    server.sendto('[%s] %s' % (ctime(),data),addr)
    addr = str(addr)
    print 'sent result to %s' % addr

server.close()






