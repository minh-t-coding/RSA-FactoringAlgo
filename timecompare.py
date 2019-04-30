import time
import utils
from Pollards import pollards
from QuadSieve import quadSieve

p = utils.genPrime(10,40)
q = utils.genPrime(10,40)
n = p*q
print(pollards.pollards(n))
print(quadSieve.quadSieve(n))
