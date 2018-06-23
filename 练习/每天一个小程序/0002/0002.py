#-*-coding:utf*8-*-
#把生成的验证码存进mysql中去
import mysql.connector

def save(list):
    conn = mysql.connector.connect(host = 'localhost',user = 'root',password = 'root',database = 'test')
    cursor = conn.cursor()
    for i in range(len(list)):
        j = str(i+1)
        cursor.execute('insert into active_code values (%s, %s)',[j,list[i]])

if __name__ == '__main__':
    f = open(u'D:\project\python\\backup\练习\每天一个小程序\\0002\code.txt', 'r')
    code = []
    for line in f.readlines():
        lines = str(line[:-1])
        code.append(lines)
    save(code)
    f.close()