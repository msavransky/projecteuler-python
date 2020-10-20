# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:58:20 2020

@author: Martin
"""

cuadradosuma = 0
sumacuadrados = 0
for i in range(101):
    cuadradosuma = cuadradosuma + i
    sumacuadrados = sumacuadrados + i**2
print(cuadradosuma**2-sumacuadrados,cuadradosuma)    