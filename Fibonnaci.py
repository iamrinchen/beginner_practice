# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 
"""

x=input("Give number")

n=int(x)

n=5

list_f=[]

for i in range(0,n):

    # print(i)

    if i==0:

        f=0

    elif i==1:

        f=1

    list_f=list_f+[f]

    f=list_f[i]+list_f[i-1]

    print(f)
