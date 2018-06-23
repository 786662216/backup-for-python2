#coding:utf-8
#这个版本没有成功，各个函数交互执行、饱和模块的导入我搞不明白  v
import time
import datetime
import 项目.weibo.RunAutomanticlly
import 项目.weibo.weiboAPI


def CreatNowTimeStr():
    TimeSecound = time.time()
    date = time.localtime(TimeSecound) #现在的具体时间
    DateMday = date[2]
    DateHour = date[3]
    str = u'''咚~咚~咚~我是老佘百分百的机器人(((o(*ﾟ▽ﾟ*)o))),现在是%d年%d月%d日%d时%d分%d秒,
    现在我只有报时功能哦~  http://www.google.com 404喽( ° △ °|||)︴'''% (date[0],date[1],DateMday,DateHour,date[4],date[5])
    return str


_
项目.weibo.RunAutomanticlly.RunByTime(项目.weibo.weiboAPI.SendWeibo(CreatNowTimeStr()))






