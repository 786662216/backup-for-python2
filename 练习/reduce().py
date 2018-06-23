def prod(l):
    return reduce(multiplication,l)
def multiplication(x,y):
    return x * y
d = [1,2,3,4,5]
print prod(d)