"""****************************************************************************
* File: RSA_Pollard_Rho.py
* Project: RSA Key, Generation and Decryption
* Author: Everest Brooks (everest1@umbc.edu)

For the final part of the project, implement the Pollard rho algorithm and 
use it to attempt to factor your fellow students' moduli. 

Your code must be able to factor the "easy" moduli that I provide, and 
factoring one or more "moderate" moduli will improve your score. Extra credit 
will be awarded for successfully factoring a classmate's modulus (other than 
your partner's, if you're working with one) or any of the "tricky" moduli.

****************************************************************************"""
import math
import random as rand

def Pollard_Rho(n):
    i = 1
    x = rand.randrange(0, n)
    y = x
    k = 2
    
    while True:
        i = i + 1
        #x = ((x-1)^2) mod n
        x = pow(x-1, 2, n)
        d = math.gcd(y - x, n)
    
        if((d != 1) and (d != n)):
            return d
    
        if(i == k):
            y = x
            k = 2*k


def main():
  
    test_names = ["test80", "test100", "test120"] 
        
    test_values = [28654659349644068479171, 208049152859353337016704626903, 45016778422508551131998204016196369]

    for i in range(len(test_values)):
        print("The factors of " + test_names[i] + " are: ")
        factor = Pollard_Rho(test_values[i])
        print(([factor, test_values[i]//factor]))
    
    input("Press Enter to exit.")

main()