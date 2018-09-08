# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:27:46 2018

@author: user


https://blog.csdn.net/joylnwang/article/details/7064115

https://blog.csdn.net/gaixm/article/details/49282711
https://blog.csdn.net/xiazdong/article/details/7986015
https://www.cnblogs.com/william-cheung/p/3472300.html

"""
import copy
A=[1,2,3,4,5,6,7,8,9]

#pm=[]

def permutaion(A):
    if len(A)==1:
        #pm.append(A)
        return [A]
    
    pm=[]
    for i in range(len(A)):
        B=copy.deepcopy(A)
        B.pop(i)
        tmp=permutaion(B)
        for k in range(len(tmp)):
            tmp[k].append(A[i])
            e=copy.deepcopy(tmp[k])
            pm.append(e)
    return pm

            
     
pms=permutaion(A)
i=1
for e in pms:
    print(i,":\t", e)
    print()
    i+=1
    