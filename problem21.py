# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:27:36 2020

@author: Martin
"""

def divisores(n):
    l = []
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    return(l)

amicable = []
for n in range(1,10001):
    if sum(divisores(sum(divisores(n))))==n and sum(divisores(n))!=n:
        amicable.append(n)
#print(sum(amicable))        

print(amicable)
print(sum(amicable))
