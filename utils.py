import random

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

def genPrime(b, r):
    """
    b: number of bits for output prime
    r: rounds of primality testing
    """

    while(True):
        # Pick random odd integer n in the range [2^(b-1), 2^b-1]
        x = random.randint(pow(2,b-1),pow(2,b)-1)
        xbin = int(bin(x)[2:])  
        xbin |= 1
        num = int(str(xbin), 2)
        if (testPrime(num, r)):
            return num

def testPrime(n, r):
    """
    Testing for primality using miller-rabin test
    Returns False if n is composite, True if "probably prime"
    pseudo-code taken from https://en.wikipedia.org/wiki/Miller-Rabin_primality_test
    """
    if n == 2:
        return True
    if (n <= 1) or (n % 2 == 0):
        return False
    
    # Get n as 2^r * d + 1
    r = 0
    d = n-1
    while (d % 2 == 0):
        r += 1
        d //= 2
    
    # Witness Loop
    for _ in range(r):
        a = random.randint(2,n-2)
        x = pow(a,d,n)
        if (x == 1) or (x == n-1):
            continue
        for _ in range (r-1):
            x = pow(x,2,n)
            if (x == n-1):
                break   # Go to next round
        else:
            return False
    return True
            
print(genPrime(250,40))
