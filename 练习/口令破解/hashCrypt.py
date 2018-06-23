#-*-coding:utf-8-*-
u'''创建一个待破解的密码本'''
import hashlib

def testpass(password):
    salt = 'salt'
    md5 = hashlib.md5()
    md5.update(password + salt)
    return md5.hexdigest()


def main():
    f1 = open('password.txt','r')
    f2 = open('encryptedpassword.txt','w')

    for line in f1.readlines():
        f2.write(testpass(line.strip('\n')) + '\n') #line默认有空格，要去掉

    f1.close()
    f2.close()

if __name__ == '__main__':
    main()