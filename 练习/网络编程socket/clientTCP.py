#coding:utf-8
from socket import *
from time import ctime


HOST ='120.76.142.240'
PORT = 2333
ADDRESS = (HOST,PORT)

client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDRESS)

while True:
    data = raw_input('>>>')
    if not data:
        break
    client.send(data)
    data = client.recv(1024)
    if not data:
        break
    print data


client.close()