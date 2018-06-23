#coding:utf-8
from socket import *
from time import ctime

HOST ='120.76.142.240'
PORT = 23333
ADDRESS = (HOST,PORT)

client = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>>>')
    if not data:
        break
    client.sendto(data,ADDRESS)
    data,ADDRESS= client.recvfrom(1024)
    if not data:
        break
    print data

client.close()