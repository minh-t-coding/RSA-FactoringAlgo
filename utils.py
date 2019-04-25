# found this code
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def modexp(b,e,m):
    """
    computes b^e mod m
    """
    b=b%m
    result=1
    val=b
    binexp=bin(e)[2:]
    
    for i in range(len(binexp)):
        if int(binexp[-i-1])==1:
            result=result*val%m
        val=val*val%m

    return result
