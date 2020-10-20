# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:03:26 2020

@author: Martin
"""

sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i

print(sum)        