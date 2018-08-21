# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:46:47 2018

@author: user
"""

'''
https://blog.csdn.net/zhangyx_xyz/article/details/50949957
LIS 低价购股票



'''

def LIS2(nums):
    size = len(nums)
    dp = []
    for x in range(size):
        low, high = 0, len(dp) - 1
        while low <= high:
            mid = (low + high) //2
            if dp[mid] >= nums[x]:
                high = mid - 1
            else:
                low = mid + 1
        if low >= len(dp):
            dp.append(nums[x])
        else:
            dp[low] = nums[x]
    return len(dp)

A=[10, 9, 2, 5, 3, 7, 101, 18]
print(LIS2(A))



def longest_increasing_subsequence(X):
    """Returns the Longest Increasing Subsequence in the Given List/Array"""
    N = len(X)
    P = [0] * N
    M = [0] * (N+1)
    L = 0
    for i in range(N):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (X[M[mid]] < X[i]):
               lo = mid+1
           else:
               hi = mid-1
 
       newL = lo
       P[i] = M[newL-1]
       M[newL] = i
 
       if (newL > L):
           L = newL
 
    S = []
    k = M[L]
    for i in range(L-1, -1, -1):
        S.append(X[k])
        k = P[k]
    return S[::-1]


def longest_increasing_subsequence_indices(seq):  # ???? replace
    from bisect import bisect_right

    if len(seq) == 0:
        return seq

    # m[j] in iteration i is the last index of the increasing subsequence of seq[:i]
    # that ends with the lowest possible value while having length j
    m = [None] * len(seq)
    predecessor = [None] * len(seq)
    best_len = 0

    for i, item in enumerate(seq):
        j = bisect_right([seq[k] for k in m[:best_len]], item)
        m[j] = i
        predecessor[i] = m[j-1] if j > 0 else None
        best_len = max(best_len, j+1)

    result = []
    i = m[best_len-1]
    while i is not None:
        result.append(i)
        i = predecessor[i]
    result.reverse()
    return result

def longest_increasing_subsequence(seq):
    return [seq[i] for i in longest_increasing_subsequence_indices(seq)]
 
if __name__ == '__main__':
    for d in [[3,2,6,4,5,1], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]]:
        print('a L.I.S. of %s is %s' % (d, longest_increasing_subsequence(d)))