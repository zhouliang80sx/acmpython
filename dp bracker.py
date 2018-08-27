# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:07:36 2018

@author: user
"""
'''

动态规划问题：添加括号使表达式的值最大
给定一个表达式（只有加法和乘法两种运算），要求通过添加括号使得表达式的值最大
譬如说100×100+100×100×100+100×100的最大值是(100×(100+100))×((100×(100+100))×100)=40000000000
 
设原计算式为: n1 op1 n2 op2 n3 op3 ... n[m-1] op[m-1] n[m]. 其中n为数字, op为操
作符(即+或*)
另设T(n[i], n[j])为第i个数和第j个数之间的子式的最大值. 则有
T(n[i], n[j]) = max{T(n[i], n[m]) op[m] T(n[m+1], n[j])} 其中m from i to j.

https://wenku.baidu.com/view/7b9ed516a2161479171128a1.html


动态规划算法例题及解析
https://blog.csdn.net/runninglion/article/details/17338409
注意两个负数相乘的结果是正数，故它们可能大于只用正数求解的结果，
但是只有做运算的两负数都尽可能的小，才能使结果尽可能的大。
为了解决表达式中有负数的问题，需要多加一个 dp矩阵，用于保存最大值和最小值。


https://segmentfault.com/a/1190000003939663
给定一个整数数组，要求在数字之间任意添加乘号，加号和括号，使得最后表达式结果最大。
比如1121,最大值为(1+1)*(2+1)，这里数字可以是0或者负数
解法和I是一样的，不过这里我们要维护一个最大表和一个最小表，这样，每次我们要乘的那
个数是正数时，我们的最大值就是之前的最大值乘以这个正数，最小值就是之前的最小值乘
以这个正数。如果要乘的是个负数的话，我们的最大值就是之前的最小值乘以这个正数
最小值就是之前的最大值乘以这个正数。另外，我们还要先初始化这个两个表，
因为之前那题结果肯定大于0，所以我们不用初始化，
不管怎么算原先矩阵中的0都会被替换掉。而本题中可以有0和负数，
所以我们要把最大表先初始化为负最大值，最小表初始化为正最小值。


https://blog.csdn.net/runninglion/article/details/17338409
分析：显然对于此题，加括号的作用是改变运算的顺序，
所以就不用考虑 +和 * 号本身的运算优先级了，
只需把精力放在表达式的分割上。
可以看出，这个问题和著名的矩阵连乘问题是非常相似的。
矩阵连乘问题的求解过程：设a[i .. j]表示 i、j区间内所有矩阵相乘所需的最小数乘次数，
则必有 a[i .. j] = a[i .. k] * a[k+1 .. j] (i <= k < j)，
因为矩阵的数乘次数只与它们的行列数有关。
而题的求解思路和矩阵连乘的求解思路是一样的，也是从部分解推导出整个运算的结果。

注意两个负数相乘的结果是正数，故它们可能大于只用正数求解的结果，
但是只有做运算的两负数都尽可能的小，才能使结果尽可能的大。
为了解决表达式中有负数的问题，需要多加一个 dp矩阵，用于保存最大值和最小值。



https://segmentfault.com/a/1190000003939663
给定一个整数数组，要求在数字之间任意添加乘号，加号和括号，
使得最后表达式结果最大。
比如1121,最大值为(1+1)*(2+1)，这里数字可以是0或者负数。


https://blog.csdn.net/u010372095/article/details/46573329
CF E. Vanya and Brackets(添加一对括号使得表达式的值最大)


'''
#import copy


def preprocess(S):
    n=len(S)
    nums=[]
    ops=[]
    temp=''
    for i in range(n):
        if S[i]=='+' or S[i]=='-' or S[i]=='*' or S[i]=='/':
            ops.append(S[i])
            nums.append(int(temp))
            temp=''
        else:
            temp=temp+S[i]
    nums.append(int(temp))
    return nums,ops

            
            

    
def maxexp(S):
    nums,ops=preprocess(S)
    n=len(nums)
    
    M=[[0 for i in range(n)] for j in range(n)]
    MMin=[[1<<64 for i in range(n)] for j in range(n)]

    MSign=[[(1,1) for i in range(n)] for j in range(n)]

    K=[[0 for i in range(n)] for j in range(n)]
    KMin=[[0 for i in range(n)] for j in range(n)]
    

    for i in range(n):
        M[i][i]=nums[i]
        MMin[i][i]=nums[i]
        MSign[i][i]=(0,0)
          

    for step in range(1,n):
        for i in range(0,n):
            j=i+step        
            if j>=n: continue
            maxValue=-1<<64
            minValue=1<<64
            for k in range(i,j):
                if ops[k]=='+':
                    M[i][j]=M[i][k]+M[k+1][j]
                    MMin[i][j]=MMin[i][k]+MMin[k+1][j]
                    if M[i][j]>maxValue:  
                        MSign[i][j]=(1,1)
                    

                    
                elif ops[k]=='-':
                    M[i][j]=M[i][k]-MMin[k+1][j]
                    MMin[i][j]=MMin[i][k]-M[k+1][j]
                    if M[i][j]>maxValue:  
                        MSign[i][j]=(1,-1)

                    
                elif ops[k]=='*':
                    mtemp=[0,0,0,0]
                    mtemp[0]=MMin[i][k]*MMin[k+1][j]
                    mtemp[1]=M[i][k]*MMin[k+1][j]
                    mtemp[2]=MMin[i][k]*M[k+1][j]
                    mtemp[3]=M[i][k]*M[k+1][j]
                    
                    M[i][j]=max(mtemp)
                    MMin[i][j]=min(mtemp)   
                    if M[i][j]>maxValue:                            
                        if M[i][j]==mtemp[0]:
                            MSign[i][j]=(-1,-1)
                        elif M[i][j]==mtemp[1]:
                            MSign[i][j]=(1,-1)
                        elif M[i][j]==mtemp[2]:
                            MSign[i][j]=(-1,1)                        

                elif ops[k]=='/':
                    mtemp=[0,0,0,0]
                    if MMin[k+1][j]!=0:
                        mtemp[0]=MMin[i][k]/MMin[k+1][j]
                        mtemp[1]=M[i][k]/MMin[k+1][j]
                    if M[k+1][j]!=0:
                        mtemp[2]=MMin[i][k]/M[k+1][j]
                        mtemp[3]=M[i][k]/M[k+1][j]

                    M[i][j]=max(mtemp)
                    MMin[i][j]=min(mtemp)                    
                    if M[i][j]>maxValue:                            
                        if M[i][j]==mtemp[0]:
                            MSign[i][j]=(-1,-1)
                        elif M[i][j]==mtemp[1]:
                            MSign[i][j]=(1,-1)
                        elif M[i][j]==mtemp[2]:
                            MSign[i][j]=(-1,1)                        

                if M[i][j]>maxValue:
                    maxValue=M[i][j]
                    K[i][j]=k

                if MMin[i][j]<minValue:
                    minValue=M[i][j]
                    KMin[i][j]=k
                    
                    
            M[i][j]=maxValue # 取k种划分的最大值
            MMin[i][j]=minValue # 取k种划分的最小值
            #MSign=[]
            
             
            
        print('\n','step=',step)
        for i in range(len(M)):
            for j in range(len(M[0])):
                print('{:8d}'.format(M[i][j]),end=',')
            print()
            
    return M,MMin,K,KMin,MSign

            
def printexp(i,j,ks): # 对'/,*'KMin的使用还未实现 
    if i==j:
        print(nums[i],end='')
        return
    
    print('(',end='')
    if MSign[i][j]==(1,1):
        printexp(i,ks[i][j],K)
        print(ops[ks[i][j]],end='')
        printexp(ks[i][j]+1,j,K)

    if MSign[i][j]==(-1,-1):
        printexp(i,ks[i][j],KMin)
        print(ops[ks[i][j]],end='')
        printexp(ks[i][j]+1,j,KMin)

    if MSign[i][j]==(1,-1):
        printexp(i,ks[i][j],K)
        print(ops[ks[i][j]],end='')
        printexp(ks[i][j]+1,j,KMin)

    if MSign[i][j]==(-1,1):
        printexp(i,ks[i][j],KMin)
        print(ops[ks[i][j]],end='')
        printexp(ks[i][j]+1,j,K)

    print(')',end='')
    
    
            
    
#nums,ops=preprocess(expression) 
#='1+2-10*1+4-60' # 1+2-10*(1+4-60)
S='4+5*9-2'
#1+2-(2*1-6)
nums,ops=preprocess(S)
M,MMin,K,KMin,MSign=maxexp(S)

printexp(0,len(M)-1,K)


