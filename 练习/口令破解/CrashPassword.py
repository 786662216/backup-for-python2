#-*-coding:utf-8-*-
u'''利用字典碰撞名密码。crack里的是字典main里的是待破解的密码。main把
待破解的MD5值传给crack，crack字典里的密码用cryptpass加密后和其相比'''

import hashlib

def CryptPass(password): #用来md5加密
    salt = 'salt'
    md5 = hashlib.md5()
    md5.update(password + salt)
    return md5.hexdigest()

def crack(CryptPassword):
    f = open('top100.txt')
    for line in f.readlines():
        crypt = CryptPass(line.strip('\n'))
        if CryptPassword == crypt:
            print "[+] Found password : %s" % line.strip('\n')
            return
    print "[-] Password not found"
    f.close()

def main():
    print "[-] Start cracking......"
    f = open("encryptedpassword.txt")
    for line in f.readlines():
        crack(line.strip('\n')) #同样要去掉换行符
    f.close()

if __name__ == "__main__":
    main()