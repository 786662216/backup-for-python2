#判断素数
def not_prime_num(n):#
    if n == 1 :
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return True
        return False
l = range(1,101)
print filter(not_prime_num,l)
