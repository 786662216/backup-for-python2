#coding:utf-8
#实验吧

import requests
import re
import time

url1 = 'http://ctf5.shiyanbar.com/jia/'

aa = requests.session()
    # .session(),如果不用session则url1和url2请求的网页是不同的，每次页面的题目是随机的
content = aa.get(url = url1).content
print aa.cookies

s = r'\(\d{4}.{47}'
p = re.compile(s)
num = p.findall(content)
print num

b = r'\d+'
q = re.compile(b)
number = q.findall(num[0])
result = (int(number[0]) + int(number[1])) * (int(number[2]) - int(number[3])) - (int(number[4]) + int(number[5]) - int(number[6])) * int(number[7])
print result

url2 = 'http://ctf5.shiyanbar.com/jia/'
data = {'pass_key' : result}

a = aa.post(url2, data = data)
print a.text