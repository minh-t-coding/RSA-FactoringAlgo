import utils
# This is an example of how RSA is implemented.

def genKeyPair(klen):
    e = 3 # Choose some e that is relatively prime to phi(n)
    p = utils.genPrime(klen//2, 40)
    q = utils.genPrime(klen//2, 40)

    while (p%e == 1):
        p = utils.genPrime(klen//2, 40)
    while (q%e == 1):
        q = utils.genPrime(klen//2, 40)

    N = p*q
    phi = (p-1)*(q-1)
    print("phi: {}".format(phi))
    d = utils.xgcd(e,phi)[1]
    if d < 0:
        d += phi
        
    return (N,e,d)

myRSA = genKeyPair(10)


N = myRSA[0]
e = myRSA[1]
d = myRSA[2]

message = 420

cipher = pow(message,e,N)

decrypt = pow(cipher,d,N)
print(decrypt)
