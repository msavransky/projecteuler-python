# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:15:35 2020

@author: Martin
"""

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

primos2mill = []
i = 2
while i < 2000000:
    if isprime(i):
        primos2mill.append(i)
    i=i+1

print('len de primos es', len(primos2mill), 'ultimo elem es', primos2mill[-1])    
print(sum(primos2mill))