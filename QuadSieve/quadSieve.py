import sieve
import linearSolverMod2
from math import gcd

def quadSieve(n):
    factor=1
    upperSieveBound=100
    while factor==1 or factor==n:
        sieveResult=sieve.sieve(n,upperSieveBound)
        smoothNumbers=sieveResult[0]
        primes=sieveResult[1]
    
        matrix=[]
        for numTup in smoothNumbers:
            expVec=[i%2 for i in numTup[2]]
            matrix.append(expVec)

        solutions=linearSolverMod2.solve(matrix)

        for solution in solutions:
            sieveExpVec=[0]*len(primes)
            originalSquare=1
            for index in solution:
                sieveExpVec=[x + y for x, y in zip(sieveExpVec, smoothNumbers[index][2])]
                originalSquare*=smoothNumbers[index][0]
            for i in range(len(sieveExpVec)):
                sieveExpVec[i]//=2
            sieveVal=1
            for i in range(len(primes)):
                sieveVal*=pow(primes[i],sieveExpVec[i])
        
            factor=gcd(abs(originalSquare-sieveVal),n)
            
        upperSieveBound*=2
        
    return {factor,n//factor}

#print(quadSieve(15347))
#print(quadSieve(61*71))
