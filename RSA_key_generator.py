"""****************************************************************************
* File: RSA_key_generator.py
* Project: RSA Key, Generation and Decryption
* Author: Everest Brooks (everest1@umbc.edu)

RSA Key Generation
This program will generate RSA public and private keys. The program will
accept the desired modulus size in bits as a parameter (e.g. 1024, 2048, 4096)
and write the keys, clearly labeled, to stdout. The Extended Euclidean
Algorithm is used to compute modular inverses and Miller-Rabin performs the 
test for probable primes.

****************************************************************************"""
import math
import random
from datetime import datetime


# helper function for finding e, etc
def gcd(a, b):
    while a != 0:
        a1 = a
        a = b % a
        b = a1
    return b


#int EUCLID(int a, int b){
#    if(b == 0)
#        return a;
#    else
#        return EUCLID(b, a % b); 
#}
def EXT_EUCLID(x, y):
    if gcd(x, y) != 1:
        return None

    a, b, c = 1, 0, x
    d, e, f = 0, 1, y

    while f != 0:
        z = c // f
        d, e, f, a, b, c = (a-z * d), (b-z * e), (c-z * f), d, e, f

    return a % y  


def MILLER_RABIN(n, s):
#   for j in range(1, s):
#       a = random.randrange(1, n-1)
#       if WITNESS(a, n):
#           return "COMPOSITE"
#   return "PRIME"

    # create num to compute with 
    d = n-1
    while d % 2 == 0:
        d = d // 2
    
    # test s times, can be changed
    for i in range(s):
        a = random.randrange(2, n-1)
        
        # pow is a^d % n
        t = pow(a, d, n)
        if t == 1 or t == n-1:
            return "PRIME"
            
        # square value until 1 or n-1 reached
        while d != n-1:
            t = (t * t) % n
            d = d * 2

            if t == 1:
                return "COMPOSITE"
            if t == n-1:
                return "PRIME"
        return "COMPOSITE"
        

def main():
    
    # get modulus size from user
    size = 0
    valid = False
    
    while valid == False: 
        size = int(input("Enter the modulus size in number of bits (1024, 2048, 4096):"))
        
        if size == 1024 or size == 2048 or size == 4096:
            valid = True
        else:
            print("Enter 1024, 2048 or 4096.") 
    
    
    # Create the primes p and q
    primality = ""
    tests = 7
    #print("creating p")
    while primality != "PRIME":
        random.seed(datetime.now())
        p = random.randrange(2**(size-1), 2**(size))
        primality = MILLER_RABIN(p, tests)

    primality = ""
    #print("creating q")
    while primality != "PRIME":
        random.seed(datetime.now())
        q = random.randrange(2**(size-1), 2**(size))
        primality = MILLER_RABIN(q, tests)

    n = p * q
   
    # compute relatively prime e using (p-1)*(q-1)
    factor = 0
    #print("creating e")
    while factor != 1:
        e = random.randrange(2**(size-1), 2**(size))
        factor = gcd(e, (p-1) * (q-1))

    # compute d using e and ext_euclid    
    #print("creating d")
    d = EXT_EUCLID(e, (p-1)*(q-1))
    
    publicKey = (n, e)
    privateKey = (n, d)
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    
    

    M = "This message has been encoded into RSA."
    x = 0
    for c in M:
        x = x << 8
        x = x ^ ord(c)
        
    M_RSA = pow(x, d, n)
    
    print("The message is signed as:", M_RSA)
    
main()   
