#coding:utf-8

def RunByTime(Funtion):

    import time
    import datetime

    SchedTime = datetime.datetime(2017,8,15,3,3,3)  #要执行的时间
    Frequency = datetime.timedelta(days=1) #频率，这个函数的参数有days,months,seconds,years,minutes都是字面意思,也可以为负

    while True:
        time.sleep(1)  # 循环执行的速度太快，虽然只有一秒但也会执行很多次,所以要等1s
        now = datetime.datetime.now() #返回值里面有微秒可把我坑惨了
        if now.date() == SchedTime.date():#先判断日期相不相同
            if (now.hour == SchedTime.hour) and (now.minute == SchedTime.minute) and (now.second == SchedTime.second):#在判断时间相不相同，主要是为了避开微秒的比较
                Funtion #这里要运行的程序
                SchedTime = SchedTime + Frequency
                print now,u"执行成功"
            else:
                pass
        else:
            pass





