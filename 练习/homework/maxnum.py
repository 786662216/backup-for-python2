#-*-coding:utf-8-*-
#第四个
m = [0,1,2,3,4,5,6,7,8,9]
n = [0,1,2,3,4,5,6,7,8,9]

def MAX(k,m,n):
    newnum = []
    for u in range(0,k):
        for i in m:
            for j in n:
                if ((i + j) <= (len(m) + len(n))):
                    newnum.append(i + j)

    return max(newnum)

if __name__ =='__main__':
    print MAX(4,m,n)




