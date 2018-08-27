# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:46:47 2018

@author: user
"""

import numpy as np
import numpy.linalg as nlg

a=[[1,2],[3,4]]
A=np.mat(a)
# inv of martrix: https://jingyan.baidu.com/article/925f8cb8a74919c0dde056e7.html


#http://blog.sina.com.cn/s/blog_70ec9a6f01012eus.html
#https://wenku.baidu.com/view/97919667680203d8cf2f2461.html
#最有子问题，求解A[i]：A[j]之间的矩阵乘法A[i:j]
# dp[i][j]=min(dp[i][k]+dp[k+1][j]+ pi*pk*pj)  for k in range(i,j)
#dp[i][j]=0 if i==j

'''
动态规划经典问题
https://www.jianshu.com/p/7ffba3910997





应用动态规划方法
下面用动态规划方法来求解矩阵链的最优括号方案，我们还是按照之前提出的4个步骤进行：
1.动态规划的第一步是寻找最优子结构，
  然后就可以利用这种子结构从子问题的最优解构造出原问题的最优解
  刻画一个最优解的结构特征
2.递归地定义最优解的值----递归公式
    下面用子问题的最优解来递归地定义原问题最优解的代价。

3.基于递归公式写出一个递归算法
计算最优解的值，通常采用自底向上的方法
自底向上表格法代替递归算法来计算最优代价

4.利用计算出的信息构造一个最优解


'''

A=[(3,5),(5,10),(10,8),(8,2),(2,4)]
def matrixmul(A):
    n=len(A)
    M=[[0 for i in range(n)] for j in range(n)]

    for step in range(1,n):
        for i in range(0,n):
            j=i+step        
            if j>=n: continue
            minValue=1000000000
            for k in range(i,j):
                M[i][j]=M[i][k]+M[k+1][j]+A[i][0]*A[k][1]*A[j][1]
                if M[i][j]<minValue:
                    minValue=M[i][j]
            M[i][j]=minValue # 取k种划分的最小值
           
        print('\n','step=',step)
        for i in range(len(M)):
            for j in range(len(M[0])):
                print('{:8d}'.format(M[i][j]),end=',')
            print()
            
    return M
    
     

M=matrixmul(A)    







