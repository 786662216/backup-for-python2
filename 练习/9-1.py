#coding:utf-8
import os
f1 = open(r"C:\Users\78666\Desktop\project\files\hellow.txt",'r')
f2 = f1.readlines()
for line in f2:
    if line[0] is '#':
        f2.remove(line)
for line in f2:
    print line
#忽略以井号开头的行