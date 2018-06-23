#-*-coding:utf-8-*-
#0001，生成200个验证码
import string
import random

# 生成一个字典，里面是大写字母和数字
upper = string.uppercase
number = string.digits
ware = upper + number  # 生成了!

def code():
    # 开始生成
    str = ''
    CODE = ''
    for j in range(5):
        for i in range(5):
            str = str + random.choice(ware) #随即取5个字符
        str = str + '-' #加上个短横线
        CODE = CODE + str
        str = ''
    CODE = CODE[0:-1] + '\n' #这个是为了去掉最后的短横线，顺便换成换行符
    #存进文件
    with open('code.txt','a') as f:
        f.write(CODE)

if __name__ =='__main__':
    for i in range(200):
        code()