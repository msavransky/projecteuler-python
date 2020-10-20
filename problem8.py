# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:52:16 2020

@author: Martin
"""

t = open('1000digitnumber.txt').read()
t = t.replace('\n','')
t = t.replace('\t','')
t = t.strip('\n')
t = t.strip('\t')
#print(t)
#print(type(int(t[50])))

lista = []

for lugar in range(988):
    prod13 = 1
    for i in range(13):
        prod13 = prod13 * int(t[i+lugar])
    lista.append(prod13)    
print(max(lista))    