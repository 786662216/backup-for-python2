# -*- coding:utf-8 -*-
import os
import random

def picture():#随机发送图片
    with open('./haha.txt', 'r') as f:
        a = f.read()
    a = a.split('\n\n')
    haha = random.choice(a)
    print haha
    a.remove(haha)
    with open('./haha.txt', 'w') as f:
        for i in a:
            if i == '' or i == '\n':
                a.remove(i)
                continue
            f.write(i)
            f.write('\n')
            f.write('\n')

for i in range(10):
    print i
    picture()