#-*-coding:utf-8-*-
#第三个
import sys
sys.setrecursionlimit(1000000)

s = '01001011'

def T(s):
    a = 0
    b = 0
    for i in s:
        if i =='0':
            a = a + 1
        elif i == '1':
            b = b + 1
    if a == len(s):
        print 'A',
    elif b == len(s):
        print 'B',
    else:
        print 'C',
        T(s[:len(s)/2])
        T(s[len(s)/2:])


if __name__ =='__main__':
    T(s)




