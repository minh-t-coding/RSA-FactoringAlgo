import sys
sys.path.append("..")

import utils
import tonellishanks
import math
import copy
from tonellishanks import tonelli
from tonellishanks import legendre


smoothBound=500
upperSieveBound=500

def sieve(n):
    smoothBound=math.ceil(n/math.log(n))
    upperSieveBound=4*math.floor(math.sqrt(n))
    primes=utils.primes(smoothBound)
    sievePrimes=[p for p in primes if legendre(n,p)==1]
    
    sqrtn=math.ceil(math.sqrt(n))
    initialSieve=[pow(x+sqrtn,2)-n for x in range(upperSieveBound)]

    expvector=[[]]*len(initialSieve)
    for i in range(len(expvector)):
        expvector[i]=[0]*len(sievePrimes)

    finalSieve=copy.deepcopy(initialSieve)
    for primeIndex in range(len(sievePrimes)):
        p=sievePrimes[primeIndex]
        
        root=tonelli(n,p)
        divisibleIndices=set()
        for r in [root,p-root]:
            a=(r-sqrtn)%p

            i=a
            while i<len(finalSieve):
                divisibleIndices.add(i)
                i+=p
        for i in divisibleIndices:
            finalSieve[i]//=p
            expvector[i][primeIndex]=1
            
    smoothNumbers=[(i+sqrtn,initialSieve[i],expvector[i]) for i in range(len(finalSieve)) if finalSieve[i]==1]
    return (smoothNumbers,sievePrimes)



        
