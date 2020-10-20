# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:20:14 2020

@author: Martin
"""
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True
    

primes = [2]
n = 3
while len(primes) <10002:
    if isprime(n):
        primes.append(n)
    n = n+1
    
print(len(primes),primes[-2])        