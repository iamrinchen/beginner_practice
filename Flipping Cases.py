# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:53:45 2023

@author: nthakur
"""

p='iF i AM HAVING AN ICECREAM. hELLO!! ! '

j=''

for s in p:
    if ord(s) in range(97,123): ## changed 122 to 123 for z
        a=chr(ord(s)-32)
    elif ord(s) in range(65,91):  ## changed 90 to 91 for Z  
        a=chr(ord(s)+32)
    
    else: 
        a=s
    j = j+a

print(j)

