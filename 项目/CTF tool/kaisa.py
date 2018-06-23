#-*-coding:utf-8-*-
import base64
import string

dic1 = string.uppercase
dic2 = string.lowercase
cipher = 'EWJ{ZWptZXdod3ZiYWZodWRjcG9jemJz}'
decode = ''

for j in range(0,26):
    for i in cipher:
        if i in dic1:
            decode = decode + chr((ord(i) - 65 + j) % 26 + 65)#注意这个写法
        elif i in dic2:
            decode = decode + chr((ord(i) - 97 + j) % 26 + 97)
        else:
            decode = decode + i
    print decode
    decode = ''
