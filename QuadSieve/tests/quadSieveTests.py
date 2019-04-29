import sys
sys.path.append('..')
sys.path.append('../..')
from quadSieve import quadSieve
from utils import primes
import random

def testRandom3Digit():
    nsamples=10
    for i in range(nsamples):
        threeDigitPrimes=primes(1000)[2:]
        random.shuffle(threeDigitPrimes)
        p1,p2=threeDigitPrimes[0],threeDigitPrimes[1]
        n=p1*p2
        print("primes: "+str(p1)+", "+str(p2))
        print(quadSieve(n))
        assert(quadSieve(n)=={p1,p2})

testRandom3Digit()
