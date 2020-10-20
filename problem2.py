# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:16:12 2020

@author: Martin
"""


fibo = [1,2]
while fibo[-1] < 4000000:
    fibo.append(fibo[-1]+fibo[-2])
    
print(fibo)    
sum = 0
for j in fibo:
    if j%2 == 0:
        sum = sum + j
print(sum)        