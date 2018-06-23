#coding:utf-8
import socket

PORT = 80
HOST = 'www.baidu.com'
ADDRESS  = (HOST,PORT)
#建立socket套接字，AF_INET是指基于网络的（其他的用不上），SOCK_STREAM是TCP连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDRESS)
s.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

buffer = [] 

while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

s.close()

header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('C:\Users/78666/Desktop/project/files/sina.html', 'wb') as f:
    f.write(html)
