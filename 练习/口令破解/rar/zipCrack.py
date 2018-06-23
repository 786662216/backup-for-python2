#-*-coding:utf-8-*-

#破解压缩包密码，就是跑字典。没有用多线程跑是大概223s跑完2890个密码。
import sys
import rarfile
from time import ctime
# from threading import Thread

reload(sys)
sys.setdefaultencoding('UTF-8')
print sys.getdefaultencoding()

def crackrar(rar,password):
    try:
        rar.extractall(pwd = password)
        return
    except:
        pass
def main():
    i = 0
    r = rarfile.RarFile('C:/Users/78666/Desktop/123123.rar')
    f = open(u'C:/Users/78666/Desktop/project/python/练习/口令破解/dictionary.txt')
    print 'starting at',ctime()
    for line in f.readlines():
        password = line.strip('\n')
        # t = Thread(target = crackrar,args = (r,password))
        # t.start()
        if result:
            print '[+] password =',password
            print 'done at',ctime()
            break
        else:
            i = i + 1
            print '[-]',password,'false',i
    print 'done at', ctime()
if __name__ == '__main__':
    main()