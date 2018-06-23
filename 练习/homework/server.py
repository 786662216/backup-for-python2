#coding:utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 2333
ADDRESS=(HOST,PORT)

server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

user = {'03161111': {'password':'123456',
                     'english':88,
                     'math':64,
                     'chinese':89},
        '03162222': {'password':'123456',
                     'english': 95,
                     'math': 54,
                     'chinese': 79
                     },
        '03163333': {'password':'123456',
                     'english': 65,
                     'math': 49,
                     'chinese': 79
                     }
        }

while True:
    print "waiting for connection······"
    client,addr = server.accept()
    #accept返回一个元组，包含一个新的socket对象和地址对
    print '···connected from:',addr

    while True:
        data = client.recv(1024)
        if data == 'LOGIN':
            data = client.recv(1024)
            for i in user:
                if i == data:
                    client.send('请输入密码')
                    data = client.recv(1024)
                    if data == user[i]['password']:
                        client.send('登陆成功')
                        while True:
                            data = client.recv(1024)
                            if data == 'QUERY':
                                data = client.recv(1024)
                                if data == '英语':
                                    data = str(user[i]['english'])
                                    client.send(data)
                                    break
                                if data == '语文':
                                    data = str(user[i]['chinese'])
                                    client.send(data)
                                    break
                                if data == '数学':
                                    data = str(user[i]['math'])
                                    client.send(data)
                                    break
                            elif data == 'QUERYAVG':
                                data = str((user[i]['english']+user[i]['chinese']+user[i]['math']) / 3)
                                client.send(data)
                                break
                    else:
                        client.send('N')
                else:
                    continue
            client.send('没有这个用户！')
            continue
        elif data == 'BYE':
            break
        else:
            continue
        #send方法发送一个字符串对象
    client.close()

