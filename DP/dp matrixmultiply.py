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

https://blog.csdn.net/crazy______/article/details/8263251
正整数N可以分解成为三个非负实数之和，即N=X+Y+Z, (X,Y,Z>=0),
求X,Y,Z使得表达式X*(Y+Z^2) 最大，Z^2表示Z的平方。

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



https://blog.csdn.net/u010372095/article/details/46573329
CF E. Vanya and Brackets(添加一对括号使得表达式的值最大)


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



