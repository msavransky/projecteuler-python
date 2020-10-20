# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:34:19 2020

@author: Martin
"""

def isPalindrome(s):
    return s == s[::-1]
mayor = 0
for i in range(999):
    for j in range(999):
        if isPalindrome(str(i*j)):
            if i*j > mayor:
                mayor = i*j
                print(mayor,i,j)