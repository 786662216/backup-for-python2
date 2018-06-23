#-*-coding:utf-8-*-

rate0 = 1.0 / 850.0 #原始概率
years = 0.0 #年数
rate = rate0

for i in range(0,10):
    AntiRate = 1.0 - rate #不中的概率
    FinaRate = 1.0 - (AntiRate ** 6) #中的概率
    years = years + 1
    rate = rate + rate0 #今年没中，概率加上一倍
    if years > 5: #最多第九阶梯
        rate = rate0 * 9
    print u'第',years,u'年摇中的概率是',round(FinaRate,4),'%'