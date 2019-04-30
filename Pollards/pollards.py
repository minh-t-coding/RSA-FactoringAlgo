import sys
sys.path.append('..')
sys.path.append('../..')
import utils
import math

def factor(num, b):
    """
    factor using Pollard's p-1 method
    num: odd number to factor
    b: smoothness cap
    """
    primeList = utils.primes(b)
    m = 1

    for prime in primeList:
        exp = math.floor(math.log(b,prime))
        m *= pow(prime,exp)

    a = 2
    g = utils.xgcd(pow(a,m,num)-1, num)[0]
    if (1 < g and g < num):
        return g
    elif (g == 1):
        # Increase B
        return -1
    elif (g == num):
        # Decrease B
        return -2

def pollards(num):
    b = 1
    while True:
        res = factor(num, b)
        if not(res == -1 or res == -2):
            break
        if res == -1:
            b += 1
        if res == -2:
            b -= 1
    return {res, num//res}
