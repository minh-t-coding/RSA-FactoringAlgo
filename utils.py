# found this code
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def primes(n):
    primeList = []
    exclusions = []
    for i in range(2, n+1):
        if i not in exclusions:
            primeList.append(i)
            for j in range(i*i, n+1, i):
                exclusions.append(j)
    return primeList

def readPrimes(filePath):
    file=open(filePath)
    primes=file.read().split()
    return [int(p) for p in primes]

