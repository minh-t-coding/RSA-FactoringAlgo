import time
import utils
import sys
import os
sys.path.append(os.path.abspath('.\\QuadSieve'))
sys.path.append(os.path.abspath('.\\Pollards'))
import quadSieve
import pollards
import csv

out = open("output.csv", "w", newline="")
fieldNames = ["Prime Bit Length","Max Pollard's Runtime (s)","Max QuadSieve Runtime (s)","# Pollard's Failures","# QuadSieve Failures"]
outWriter = csv.DictWriter(out, fieldnames = fieldNames)
outWriter.writerow({name: name for name in fieldNames})

bitlength = 6
sampleSize = 5
niterations = 7
bitincrement = 5
for i in range(niterations):
    polFailures = quadFailures = 0
    polMaxTime = quadMaxTime = 0

    for sample in range(sampleSize):
        q = p = utils.genPrime(bitlength, 40)
        while q == p:
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

        # data analysis
        if p_res != {p, q}:
            polFailures += 1
        else:
            polMaxTime = max(polMaxTime, ptime)
        if q_res != {p, q}:
            quadFailures += 1
        else:
            quadMaxTime = max(quadMaxTime, qtime)

    writeData = {"Prime Bit Length": bitlength,
                 "Max Pollard's Runtime (s)": '{0:.5f}'.format(polMaxTime),
                 "Max QuadSieve Runtime (s)": '{0:.5f}'.format(quadMaxTime),
                 "# Pollard's Failures": polFailures,
                 "# QuadSieve Failures": quadFailures}
    outWriter.writerow(writeData)
    bitlength += bitincrement
    
out.close()
