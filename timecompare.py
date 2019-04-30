import time
import utils
import sys
import os
sys.path.append(os.path.abspath('.\\QuadSieve'))
sys.path.append(os.path.abspath('.\\Pollards'))
import quadSieve
import pollards

bitlength = 5
for i in range(4):
    p = utils.genPrime(bitlength, 40)
    q = utils.genPrime(bitlength, 40)
    n = p*q

    print("p: {}\nq: {}\nn: {}\n".format(p,q,n))

    start = time.time()
    p_res = pollards.pollards(n)
    end = time.time()
    ptime = end-start
    print("Time for Pollard's p-1 algorithm to factor n: {}s".format(ptime))
    print("Pollards result: {}".format(p_res))

    start = time.time()
    q_res = quadSieve.quadSieve(n)
    end = time.time()
    qtime = end-start
    print("Time for Quad. Sieve algorithm to factor n: {}s".format(qtime))
    print("Quad. Sieve result: {}\n\n".format(q_res))

    bitlength *= 2
    
