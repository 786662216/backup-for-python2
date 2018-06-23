#coding:utf-8
import random
import string

str1 = 'abcdefgh'
k = '001010101010110100100110'
i = random.choice(k)
print 'i = ' + i

def collpose(): #i==0时，从左到右加密
    a = str1[:len(str1)/2]
    b = str1[len(str1)/2:]

    return str(a[::-1]) + '\n' + b

def anticollpose(): #i==1时，从右到左加密
    a = str1[:len(str1)/2]
    b = str1[len(str1)/2:]

    return str(b[::-1]) + '\n' + a

def main():
    if i == '1':
        print collpose()
    else :
        print anticollpose()

if __name__ == '__main__':
    main()
