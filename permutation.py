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

#pm=[]

def permutation(A):
    if len(A)==1:
        #pm.append(A)
        return [A]
    
    pm=[]
    for i in range(len(A)):
        B=copy.deepcopy(A)
        B.pop(i)
        tmp=permutation(B)
        for k in range(len(tmp)):
            tmp[k].append(A[i])
            #e=copy.deepcopy(tmp[k])
            pm.append(tmp[k])
    return pm




def permutation2(A):
    if len(A)==1:
        #pm.append(A)
        return [A]
    
    pm=[]
    tmp=permutation2(A[1:])
    
    for k in range(len(tmp)):
        for i in range(len(A)):
            temp=tmp[k][:]
            temp.insert(i, A[0])
            pm.append(temp)            
    return pm
            

'''
使用字典序输出全排列的思路是，
首先输出字典序最小的排列，然后输出字典序次小的排列，……，
最后输出字典序最大的排列。
这里就涉及到一个问题，对于一个已知排列，
如何求出其字典序中的下一个排列。这里给出算法。

对于排列a[1...n]，找到所有满足a[k]<a[k+1](0<k<n-1)的k的最大值，
如果这样的k不存在，则说明当前排列已经是a的所有排列中字典序最大者，
所有排列输出完毕。
在a[k+1...n]中，
寻找满足这样条件的元素l，
使得在所有a[l]>a[k]的元素中，a[l]取得最小值。
也就是说a[l]>a[k]，但是小于所有其他大于a[k]的元素。
交换a[l]与a[k].
对于a[k+1...n]，反转该区间内元素的顺序。
也就是说a[k+1]与a[n]交换，a[k+2]与a[n-1]交换，……，
这样就得到了a[1...n]在字典序中的下一个排列。


1）从排列的右端开始，找出第一个比右边数字小的数字的序号j
（j从左端开始计算），即  j=max{i|p[i]<p[i+1]}
2）在p[j]的右边的数字中，找出所有比p[j]大的数中最小的数字p[k]，
即 k=max{i|p[i]>p[j]}（右边的数从右至左是递增的，因此k是所有大于p[j]的数字中序号最大者）

3）对换pj，pk
 
4）再将[pj+1]......p[k-1]p[k]p[k+1]p[n]倒转得到排列
p''=p[1]p[2].....p[j-1]p[j]p[n].....p[k+1]p[k]p[k-1].....p[j+1]，
这就是排列p的下一个下一个排列。
 
'''

def permutation3(p):
    p.sort()
    pms=[]
    pms.append(p[:])
    
    flag=True
    length=len(p)
    while flag==True:
        j=length-2
        while j>=0 and p[j]>p[j+1] :
            j-=1
        if j==-1:
            flag=False
            break
        
        k=length-1
        for i in range(length-1,j,-1):
            if p[i]>p[j]:
                k=i
                break
            
        p[j],p[k]=p[k],p[j]
        
        mid=(j+1+length-1)//2
        for i in range(j+1,mid+1,1):
            p[i],p[j+1+length-1-i]=p[j+1+length-1-i],p[i]
        
        pms.append(p[:])
    
    return pms
            
    
        
        
        
A=[1,2,3,4,5,6,7,8,9]
     
pms=permutation3(A)

print(pms[-1])

# =============================================================================
# i=1
# for e in pms:
#     print(i,":\t", e)
#     print()
#     i+=1
#     
# =============================================================================
