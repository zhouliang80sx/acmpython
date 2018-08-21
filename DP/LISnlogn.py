# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:54:48 2018

@author: Administrator
"""


# Python program to find
# length of longest
# increasing subsequence
# in O(n Log n) time
 
# Binary search (note
# boundaries in the caller)
# A[] is ceilIndex
# in the caller

from __future__ import print_function
#############################
# Author: Aravind Kashyap
# File: lis.py
# comments: This programme outputs the Longest Strictly Increasing Subsequence in O(NLogN)
#           Where N is the Number of elements in the list 
#############################
def CeilIndex(v,l,r,key):
	while r-l > 1:
		m = (l + r)//2
		if v[m] >= key:
			r = m
		else:
			l = m
	
	return r
	

def LongestIncreasingSubsequenceLength(v):
    if(len(v) == 0):
        return 0	
	
    tail = [0]*len(v)
    pre=[-1]*len(v)
    length = 1
	
    tail[0] = v[0]
	
    for i in range(1,len(v)):
        if v[i] < tail[0]:
            tail[0] = v[i]
        elif v[i] > tail[length-1]:
            tail[length] = v[i]
            pre[length]=tail[length-1]			
            length += 1
        else:
            r=CeilIndex(tail,-1,length-1,v[i])
            tail[r] = v[i]
            pre[r]=tail[r-1]

    print(v)
    print(tail)
    print(pre)
    return length
	

v = [2, 5, 3, 7, 11, 8, 10, 13, 6]
print(LongestIncreasingSubsequenceLength(v))


def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)    # offset by 1 (j -> j-1)
    P = [None] * len(seq)

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    # the first element.
    L = 1
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # Binary search: we want the largest j <= L
        #  such that seq[M[j]] < seq[i] (default j = 0),
        #  hence we want the lower bound at the end of the search process.
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    # this will also set the default value to 0

        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Building the result: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]    # reversing





# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 16:26:29 2018
import random
import math
from collections import deque  #dq=deque()
import queue   #pq = Q.PriorityQueue()
import copy
import heapq  #heapq.heappush(heap, item), heapq.heappop(heap),heapq.heapify(x)

@author: zbc
"""
#https://blog.csdn.net/qq_31881469/article/details/77892324
#https://blog.csdn.net/wangdd_199326/article/details/76464333


#最长公共子序列 LCS  和Longest Common Subsequence
def lcs(arr, brr):
    l1 = len(arr)
    l2 = len(brr)
    if l1 == 0 or l2 == 0:
        return 0
 
    tmp_list_1 = [0] * (l1 + 1)
    tmp_list_2 = [0] * (l1 + 1)
 
    for i in range(l2):
        for j in range(l1):
            ele2 = brr[i]
            ele1 = arr[j]
            if ele2 == ele1:
                tmp_list_2[j + 1] = tmp_list_1[j] + 1
            else:
                tmp_list_2[j + 1] = max(tmp_list_2[j], tmp_list_1[j])
        tmp_list_1 = tmp_list_2
        tmp_list_2 = [0] * (l1 + 1)
 
    return tmp_list_1[l1]
 
 
arr = list('GCCCTAGCG')
brr = list('GCGCAATG')
#print (lcs(arr, brr))

def LCS(A,B):
    m=len(A)
    n=len(B)
    dp=[[0 for x in range(n+1)] for x in range(m+1)]
    
# =============================================================================
#     for line in dp:
#         print(line)
#     print()
# =============================================================================
    
    for i in range(1,m+1):
         for j in range(1,n+1):
             if A[i-1]==B[j-1]:
                 dp[i][j]=dp[i-1][j-1]+1
             else:
                 dp[i][j]=max(dp[i-1][j],dp[i][j-1])
         
# =============================================================================
#          for line in dp:
#              print(line)
#              print()
#     
# =============================================================================
                 
# =============================================================================
#     for line in dp:
#         print(line)
#         print()                 
#                          
#     print('. ',end=', ')
#     for i in range(len(B)):
#         print(B[i],end=', ')
#     print()
#                        
#     k=0           
#     for line in dp[1:]:
#         print(A[k],end=' , ')
#         for i in range(1,len(line)):
#             print(line[i],end=', ')
#         print()
#         k+=1
#         
# =============================================================================
        
    length=dp[m][n]
    rt=[None for i in range(length)]
    
    col=n
    row=m
    
    for k in range(length):
        while dp[row][col]==dp[row-1][col]:
            row-=1
        while dp[row][col]==dp[row][col-1]:
            col-=1        
        
        rt[length-1-k]=A[row-1]
        k+=1
        row-=1
        col-=1
    
    print('\nLongest Common Subsequence:\n',rt)    
    print('\nLCS length:',len(rt))
    return rt
        
        
        
    
    
#A= list('advantage') 
#B= list('didatical')
A='abcde'
B='abcfe'
#LCS(A,B)

    

#最长公共子串  Longest Common Substring
#移动法 https://blog.csdn.net/wangdd_199326/article/details/76464333
def LCSub(A,B):
    m=len(A)
    n=len(B)
    dp=[[0 for x in range(n+1)] for x in range(m+1)]
    
# =============================================================================
#     for line in dp:
#         print(line)
#     print()
# =============================================================================

    for i in range(1,m+1):
         for j in range(1,n+1):
             if A[i-1]==B[j-1]:
                 dp[i][j]=dp[i-1][j-1]+1
             else:
                 dp[i][j]=0
# =============================================================================
#     for line in dp:
#         print(line)
#     print()                 
# =============================================================================


# =============================================================================
#     print('. ',end=', ')
#     for i in range(len(B)):
#         print(B[i],end=', ')
#     print()
#                                          
#     k=0           
#     for line in dp[1:]:
#         print(A[k],end=' , ')
#         for i in range(1,len(line)):
#             print(line[i],end=', ')
#         print()
#         k+=1
# =============================================================================
    
    maxlen=-1 
    pos=(-1,-1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if dp[i][j]>maxlen:
                maxlen=dp[i][j]
                pos=(i,j)
    
    rt=''
    col=pos[1]-maxlen
    for i in range(maxlen):
        rt+=str(B[col+i])
    
    print('Longest Common Substring:\n',rt)
    return rt

            
            
                 
A='abcdefghklkjxy'
B='uafbcfklmeflgkkyx'
#LCSub(A,B)                 
                 
   
        


#最长递增（上升）子序列LIS  
#https://blog.csdn.net/u013178472/article/details/54926531
#https://blog.csdn.net/tterminator/article/details/50957527
#https://blog.csdn.net/qq_34342154/article/details/77132137
#nlogN https://blog.csdn.net/virtual_func/article/details/50912316
#（维护长度为 i 的递增子序列的最后一个元素（只维护长度为i 的递增子序列中最小的最后一个元素）。）
#https://blog.csdn.net/Sara_YF/article/details/51373401

def LIS(A):
    
    B=set(A)
    B=list(B)
    B.sort()
    A=list(A)
    return(LCS(A,B))
    
    
    
def LIS2(A):
    N=len(A)
    dp=[1 for x in range(N)]
    
    for i in range(1,N):
        for j in range(0,i):
            if A[i]> A[j]:
                dp[i]=max(dp[j]+1,dp[i])
            
    maxlen=0
    for i in range(N):
        if dp[i]>maxlen:
            maxlen=dp[i]
            
    print("LIS length:",maxlen)
    rt=[]
    k=maxlen
    for i in range(N-1,-1,-1):
        if dp[i]==k:
            rt.append(A[i])
            k=k-1
            if k==0: break
        
    rt.reverse()
    print("LIS:\n",rt)    
        
        
            
            
            
            
        
    

import time
import random
#A='axbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmastaxbdcbdxeyfughijklmxnyxowesrptqyxsurnbmast'
s='294737642947376429473764294737642947376429473764294737642947376429473764294737642947376429473764294737642947376429473764294737642947376429473764294737642947376429473764294737642947376429473764'

N=10000
A=[random.randint(1,100000) for x in range(N)]
B=sorted(A)

print('len of A:',len(A))
t1=time.time()
LIS(A)
print('LIS time',time.time()-t1)


print('--------------------------------------------------')

print('len of A:',len(A))
t1=time.time()
LIS2(A)
print('LIS2 time',time.time()-t1)




#和最大的连续子序列 #https://blog.csdn.net/wangdd_199326/article/details/76464333
#http://www.cnblogs.com/zhangchaoyang/articles/2012070.html




