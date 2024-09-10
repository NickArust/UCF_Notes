import math
def func():
    x0 = 1
    for i in range(10):
        xn = x0/(1+x0) + 1
        print( xn)
        x0 = xn

func()