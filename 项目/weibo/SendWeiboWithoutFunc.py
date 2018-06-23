# coding:utf-8
#这个版本成功了，注意每个微博API都有返回值

from 项目.weibo import APIClient
import time #可忽略
import datetime
import random

APP_KEY = 'XXXXXXXXXX' # app key
APP_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX' # app secret
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' # callback url

access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
expires_in = 1660225135
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
client.set_access_token(access_token, expires_in)

schedtime = datetime.datetime(2017,8,15,3,3,3)  # 要执行的时间
Frequency = datetime.timedelta(days=1)  # 频率，这个函数的参数有days,months,seconds,years,minutes都是字面意思,也可以为负

while True:
    time.sleep(1)  # 循环执行的速度太快，虽然只有一秒但也会执行很多次,所以要等1s

    TimeSecound = time.time() #这个确实没啥用
    date = time.localtime(TimeSecound)  # 现在的具体时间
    DateMday = date[2]
    DateHour = date[3]

    str = u'''咚~咚~咚~我是老佘百分百的机器人%s,现在是%d年%d月%d日%d时%d分%d秒,
    现在我只有报时功能哦~  http://www.google.com 404喽%s''' % (random.choice(
        [u'(๑•̀ㅂ•́)و✧', u'ヾ(≧▽≦*)o ', u'o(*≧▽≦)ツ ', u'(o゜▽゜)o☆', u'<(￣︶￣)>', u'o(*￣▽￣*)o ', u'(｡･∀･)ﾉﾞ', u'ヾ(≧∇≦*)ゝ',
         u'Hi~ o(*￣▽￣*)ブ ', u'(≧∀≦)ゞ', u'ε(*´･∀･｀)зﾞ', u'(～￣▽￣)～ ', u'︿(￣︶￣)︿', u'(/≧▽≦)/', u'(ﾉ*･ω･)ﾉ',
         u'o(〃\'▽\'〃)o ', u'o(￣▽￣)ｄ ', u'o(^▽^)o']), date[0], date[1], DateMday, DateHour, date[4], date[5],
                                                    random.choice([u'w(ﾟДﾟ)w', u'Ｏ(≧口≦)Ｏ', u'Σ(｀д′*ノ)ノ', u'ヽ(*。>Д<)o゜',
                                                                   u'┻━┻︵╰(‵□′)╯︵┻━┻', u'φ(-ω-*)', u'(σ｀д′)σ',
                                                                   u'(#`O′)', u'( >ρ < ”)', u'o(一︿一+)o', u'(#`O′) ',
                                                                   u'(＞﹏＜)', u'(；′⌒`) ', u'（；´д｀）ゞ', u'Σ( ° △ °|||)︴',
                                                                   u'(lll￢ω￢)', u'…（⊙＿⊙；）…', u'_〆(´Д｀ ) ',
                                                                   u'Σ(っ °Д °;)っ', u'(・-・*)', u'(°ー°〃) ',
                                                                   u'(((φ(◎ロ◎;)φ)))', u'o((⊙﹏⊙))o.', u'ヽ(*。>Д<)o゜ ', ]))
    now = datetime.datetime.now()  # 返回值里面有微秒可把我坑惨了
    if now.date() == schedtime.date():  # 先判断日期相不相同
        if (now.hour == schedtime.hour) and (now.minute == schedtime.minute) and (now.second == schedtime.second):  # 在判断时间相不相同，主要是为了避开微秒的比较
            client.statuses.share.post(status=str)  # 这是有返回值的
            schedtime = schedtime + Frequency
            print now, u"sent successfully"
        else:
            pass
    else:
        pass
