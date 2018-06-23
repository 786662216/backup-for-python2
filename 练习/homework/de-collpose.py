#coding:utf-8

import random
import string

i = '1'
str1 = 'dcba\nefgh'

def decollpose():
    a = str1[:len(str1)/2]
    b = str1[len(str1)/2 :]

    print a[::-1] + b

def deanticollpose():
    a = str1[:len(str1) / 2]
    b = str1[len(str1) / 2 :]

    print b + a[::-1]

def main():
    if i == '1':
        decollpose()
    else :
        deanticollpose()

if __name__ =='__main__':
    main()