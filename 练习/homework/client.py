# coding:utf-8
from socket import *
from time import ctime

print 'CONNECT:'
HOST = raw_input('请输入IP地址')
PORT = raw_input('请输入端口号')

# HOST ='120.76.142.240'
# PORT = 2333
ADDRESS = (HOST,PORT)

client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDRESS)

while True:
    print '欢迎来到学生成绩查询系统！请输入命令后回车进行下一步操作。\n' \
          'LOGIN：登录，回车后输入用户名 \n' \
          'BYE：退出查询系统，断开与服务器的连接。\n'
    data = raw_input('>>>')
    if not data:
        print '命令为空！'
        continue
    elif (data == 'LOGIN'):
        client.send(data)
        print '请输入用户名：'
        data = raw_input('>>>')
        client.send(data)
        data = client.recv(1024)
        if data == '请输入密码':
            print '请输入密码：'
            data = raw_input('>>>')
            client.send(data)
            data = client.recv(1024)
            if data == '登陆成功':
                print '欢迎！' + data
                print 'QUERY：查询特定科目，回车后输入科目名称 \n' \
                      'QUERYAVG：查询此用户所有科目的平均成绩并提示 \n' \
                      'BREAK: 退出当前用户'
                while True:
                    print '请输入查询命令'
                    data = raw_input('>>>')
                    if data == 'BREAK':
                        break
                    else:
                        if data == 'QUERY':
                            client.send(data)
                            subject = raw_input('请输入要查询的科目:')
                            data = subject
                            client.send(data)
                            data = client.recv(1024)
                            print subject +':'+ data
                        elif data == 'QUERYAVG':
                            client.send(data)
                            data = client.recv(1024)
                            print '你的平均分：' + data
            else:
                print '密码错误！'
                continue
        else:
            print '没有这个用户！'
            continue
    elif (data == 'BYE'):
        client.send(data)
        print 'BYE!'
        client.close()
        break
    else:
        print '命令无效'
        continue

client.close()

