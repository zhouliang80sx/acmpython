# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:10:06 2018

@author: Administrator
"""

#LIS nlogn 算法， 加括号求表达式最大值的DP程序，
# 求解线性方程组的Python
# 列举排列组合的程序


 
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

""" 
Let arr[0..n-1] be the input array and L(i) be the length of the LIS ending at 
index i such that arr[i] is the last element of the LIS.
Then, L(i) can be recursively written as:
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.
To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.
Thus, we see the LIS problem satisfies the optimal substructure property as the
 main problem can be solved using solutions to subproblems.

Following is a simple recursive implementation of the LIS problem. It follows 
the recursive structure discussed above.




To make use of recursive calls, this function must return
 two things:
 1) Length of LIS ending with element arr[n-1]. We use
 max_ending_here for this purpose
 2) Overall maximum as the LIS may end with an element
 before arr[n-1] max_ref is used this purpose.
 The value of LIS of full array of size n is stored in
 *max_ref which is our final result """
 
# global variable to store the maximum
global maximum
 
def _lis(arr , n ):
 
    # to allow the access of global variable
    global maximum
 
    # Base Case
    if n == 1 :
        return 1
 
    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1
 
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = _lis(arr , i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res +1
 
    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum , maxEndingHere)
 
    return maxEndingHere
 
def lis(arr):
 
    # to allow the access of global variable
    global maximum
 
    # lenght of arr
    n = len(arr)
 
    # maximum variable holds the result
    maximum = 1
 
    # The function _lis() stores its result in maximum
    _lis(arr , n)
 
    return maximum
 
def LIS(A):
    length=len(A)    
    dp=[1 for i in range(length)]
    maxlen=1
    maxindex=-1
#L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
#L(i) = 1, if no such j exists.
    for i in range(1,length):
        for j in range(0,i):
            if A[j]<A[i]:
                dp[i]=max(dp[i],dp[j]+1)
                if dp[i]>maxlen:
                    maxlen=dp[i]
                    maxindex=i

    
    rt=[None for i in range(maxlen)]
    k=0
    for i in range(length,-1,-1):
        if A[i]==maxlen-k:
            rt[maxlen-1-k]=A[i]
            k+=1
            if k==maxlen:break
        
            
    print(rt)            
    return maxlen                
        
# Driver program to test the above function
arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
n = len(arr)
print ("Length of lis is ", lis(arr))
print(LIS(arr))