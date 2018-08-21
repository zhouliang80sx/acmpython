# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:30:52 2018

@author: user

#矩阵的初等变换 https://wenku.baidu.com/view/3f9585de9f3143323968011ca300a6c30d22f15c.html

#LU矩阵求逆 https://wenku.baidu.com/view/d8cf99300b1c59eef9c7b433.html

inv: https://www.cnblogs.com/xiaoxi666/p/6421228.html
LU : 
    https://blog.csdn.net/xx_123_1_rj/article/details/39553809
    
    矩阵的QR分解（三种方法）Python实现 
    https://www.cnblogs.com/qw12/p/6079244.html
    
    https://blog.csdn.net/Mr_KkTian/article/details/52723738
    
    矩阵分解 三角分解(LU分解)
    https://blog.csdn.net/billbliss/article/details/78559289
    
    
    https://blog.csdn.net/qq_30981697/article/details/71545519
    
    
    https://www.cnblogs.com/tiandsp/archive/2011/12/02/2271751.html
    
    对矩阵分解的粗浅理解之LU分解
    https://blog.csdn.net/lsgo_myp/article/details/53856946
    
    
    https://blog.csdn.net/xckkcxxck/article/details/78701515
    
    LU分解初步
    https://blog.csdn.net/u010945683/article/details/45803141
    
--------------------------------------------------

     演示 Fabric.js demos · Matrix transformation

    http://fabricjs.com/matrix-transformation
    http://www.paufler.net/brettcode/paperjs_tutorial/paperJS-012-AffineTransformDemo.html
    

    https://scilab.io/computer-vision-image-transform/


    二维图形的矩阵变换（一）——基本概念
    https://www.cnblogs.com/TianFang/p/3920734.html
    
    python Affine transform of an image
    https://matplotlib.org/gallery/images_contours_and_fields/affine_image.html
    https://matplotlib.org/api/transformations.html#matplotlib.transforms.Affine2D
    
    Understanding the Transformation Matrix in Flash 8
    http://www.senocular.com/flash/tutorials/transformmatrix/

    Affine and Projective Transformations
    https://www.graphicsmill.com/docs/gm/affine-and-projective-transformations.htm#DifferenceBetweenProjectiveAndAffine


    Understanding Affine Transformations With Matrix Mathematics
    https://code.tutsplus.com/tutorials/understanding-affine-transformations-with-matrix-mathematics--active-10884

    
    图形的矩阵变换
    https://wenku.baidu.com/view/c30daae3fad6195f302ba6fe.html
  
    几何变换详解
    https://www.cnblogs.com/graphics/archive/2012/08/08/2609005.html
    
    matlab Matrix Representation of Geometric Transformations
    https://ww2.mathworks.cn/help/images/matrix-representation-of-geometric-transformations.html
    
    图形变换的矩阵方法
    http://www.docin.com/p-1759892258.html
    
    仿射变换
    https://www.cnblogs.com/ghj1976/p/5199086.html
    https://homepages.inf.ed.ac.uk/rbf/HIPR2/affine.htm
    
    
    
    图像处理04-几何变换详解.ppt
    https://max.book118.com/html/2016/0513/42835199.shtm
    
    The Transformation Matrix for 2D Games
    https://www.alanzucconi.com/2016/02/10/tranfsormation-matrix/
    
    数字图像处理笔记与体会（三）——图像的几何变换
    https://www.cnblogs.com/IClearner/p/6842334.html
    https://blog.csdn.net/yangtao2076/article/details/51912014
    
    
    
    
"""

import numpy as np
import numpy.linalg as nlg
import random    
import time


import copy
class Matrix:
  '''矩阵类'''
  def __init__(self, row=0, column=0, fill=0.0):
    self.shape = (row, column)
    self.row = row
    self.column = column
    self._matrix = [[fill]*column for i in range(row)]
    self.I=None
    self.dt=None
    self.rank=None
    
  #用array初始化matrix 矩阵 
  def fillwith(self,array):
      self._matrix=copy.deepcopy(array)
      self.row=len(array)
      self.column=len(array[0])
      self.shape=(self.row,self.column)
      self.I=None
      self.dt=None
      self.rank=None
      
      
  def __getitem__(self, index):#chongzai []
       
    if isinstance(index, int):
      return self._matrix[index-1]
    elif isinstance(index, tuple):
      return self._matrix[index[0]-1][index[1]-1]  
    
  # 设置元素m(i,j)的值为s: m[i, j] = s
  def __setitem__(self, index, value):
    if isinstance(index, int):
      self._matrix[index-1] = copy.deepcopy(value)
    elif isinstance(index, tuple):
      self._matrix[index[0]-1][index[1]-1] = value
    self.dt=None
    self.I=None
    self.rank=None
      
  def __eq__(self, N): # ==
    '''相等'''
    # A == B
    assert isinstance(N, Matrix), "类型不匹配，不能比较"
    
    if N.shape != self.shape: # 比较维度，可以修改为别的
        return False
    for i in range(1,self.row+1):
        for j in range(1,self.column+1):
            if self[i,j]!=N[i,j]:
                return False
    return True

  def __add__(self, N):# +
    '''加法'''
    # A + B
    assert N.shape == self.shape, "维度不匹配，不能相加"
    M = Matrix(self.row, self.column+1)
    for r in range(1,self.row+1):
      for c in range(1,self.column+1):
        M[r, c] = self[r, c] + N[r, c]
    return M

  def __sub__(self, N): # -
    '''减法'''
    # A - B
    assert N.shape == self.shape, "维度不匹配，不能相减"
    M = Matrix(self.row, self.column)
    for r in range(1,self.row+1):
      for c in range(1,self.column+1):
        M[r, c] = self[r, c] - N[r, c]
    return M

  def __mul__(self, N):
    '''乘法'''
    # A * B (或：A * 2.0)
    if isinstance(N, int) or isinstance(N,float):
      M = Matrix(self.row, self.column)
      for r in range(1,self.row+1):
        for c in range(1,self.column+1):
          M[r, c] = self[r, c]*N
    else:
      assert N.row == self.column, "维度不匹配，不能相乘"
      M = Matrix(self.row, N.column)
      for r in range(1,self.row+1):
        for c in range(1,N.column+1):
          sum = 0
          for k in range(1,self.column+1):
              assert 0<c<=N.column and 0<k<=N.row, "数组访问越界"
              sum += self[r, k] * N[k, c]
          M[r, c] = sum
    return M

  def __div__(self, N):
    '''除法'''
    # A / B
    pass

  def __pow__(self, k):
    '''乘方'''
    # A**k
    assert self.row == self.column, "不是方阵，不能乘方"
    M = copy.deepcopy(self)
    for i in range(k-1):
      M = M * self
    return M

  def getrank(self):
    '''矩阵的秩'''
    pass

  def trace(self):
    '''矩阵的迹'''
    N=min(self.column,self.row)
    tr=1
    for i in range(1,N+1):
        tr*=self[i,i]
        
    return tr

  def adjoint(self):
    '''伴随矩阵'''
    pass


  def invert(self):
    '''逆矩阵'''
    assert self.row == self.column, "不是方阵"
    if self.I!=None:
        return self.I
    
    M = Matrix(self.row, self.column*2)
    I = self.identity() # 单位矩阵

    #I.show()#############################
    # 拼接
    for r in range(1,M.row+1):
      temp = self[r]
      temp.extend(I[r])
      M[r] = copy.deepcopy(temp)
    #M.show()#############################
    # 初等行变换
    for r in range(1, M.row+1):
      # 本行首元素(M[r, r])若为 0，则向下交换最近的当前列元素非零的行
      #print(M)
      if M[r, r] == 0:
        for rr in range(r+1, M.row+1):
          if M[rr, r] != 0:
            #print('交换两行')  
            M[r],M[rr] = M[rr],M[r] # 交换两行
          break
      assert M[r, r] != 0, '矩阵不可逆'
      # 本行首元素(M[r, r])化为 1
      temp = M[r,r] # 缓存
      for c in range(r, M.column+1):
        M[r, c] /= temp
        #print("M[{0}, {1}] /= {2}".format(r,c,temp))
      #print(M)#show()
      # 本列上、下方的所有元素化为 0
      for rr in range(1, M.row+1):
        temp = M[rr, r] # 缓存
        for c in range(r, M.column+1):
          if rr == r:
            continue
          M[rr, c] -= temp * M[r, c]
          #print("M[{0}, {1}] -= {2} * M[{3}, {1}]".format(rr, c, temp,r))
        #print(M)#M.show()
    # 截取逆矩阵
    N = Matrix(self.row,self.column)
    for r in range(1,self.row+1):
      N[r] = M[r][self.row:]
    return N

    

  def det(self):
    if self.dt!=None:
        return self.dt
    assert self.row == self.column, "不是方阵"
    
    sign=1
    M = Matrix(self.row, self.column)
    M=copy.deepcopy(self)
    

    for r in range(1, M.row+1):
      # 本行首元素(M[r, r])若为 0，则向下交换最近的当前列元素非零的行
      #print(M)
      if M[r, r] == 0:
        for k in range(r+1, M.row+1):
          if M[k, r] != 0:
            #print('主元为0，需要交换两行:')  
            M[r],M[k] = M[k],M[r] # 交换两行
            sign*=-1 # 行交换后，det值需要反号
            #print(M)
          break
      
      if M[r,r]==0: #行初等变换后成上三角阵后，对角线上有0元素， 
          self.rank=r-1
          self.dt=0
          return 0
               
      for rr in range(r+1, M.row+1):
        temp = M[rr, r]/M[r,r] # 缓存
        for c in range(r, M.column+1):
          M[rr, c] -= temp * M[r, c]
          
    return M.trace()*sign

    
  
  def jieti(self):
    '''行简化阶梯矩阵'''
    pass

  def transpose(self):
    '''转置'''
    M = Matrix(self.column, self.row)
    for r in range(self.column):
      for c in range(self.row):
        M[r, c] = self[c, r]
    return M

  def cofactor(self, row, column):
    '''代数余子式（用于行列式展开）'''
    assert self.row == self.column, "不是方阵，无法计算代数余子式"
    assert self.row >= 3, "至少是3*3阶方阵"
    assert row <= self.row and column <= self.column, "下标超出范围"
    M = Matrix(self.column-1, self.row-1)
    for r in range(1,self.row+1):
      if r == row:
        continue
      for c in range(1,self.column+1):
        if c == column:
          continue
        rr = r-1 if r > row else r
        cc = c-1 if c > column else c
        M[rr, cc] = self[r, c]
    return M

  def det2(self):
    '''计算行列式(determinant)'''
    if self.dt!=None:
        return self.dt
    
    assert self.row == self.column,"非行列式，不能计算"
    if self.shape == (2,2):
      return self[1,1]*self[2,2]-self[1,2]*self[2,1]
    else:
      sum = 0.0
      for c in range(1,self.column+1):
        if c%2==1:sign=1
        else: sign=-1
        sum += sign*self[1,c]*self.cofactor(1,c).det2()
      return sum
  
  #@staticmethod
  def zeros(self):
    '''全零矩阵'''
    M = Matrix(self.column, self.row, fill=0.0)
    return M
  def ones(self):
    '''全1矩阵'''
    M = Matrix(self.column, self.row, fill=1.0)
    return M
  def identity(self):
    '''单位矩阵'''
    assert self.row == self.column, "非n*n矩阵，无单位矩阵"
    M = Matrix(self.column, self.row)
    for r in range(self.row):
      for c in range(self.column):
        M[r, c] = 1.0 if r == c else 0.0
    return M

  def show(self):
    '''打印矩阵'''
    for r in range(self.row):
      for c in range(self.column):
        print(self[r+1, c+1],end=' ')
      print()

      
  def __repr__(self):
    '''打印矩阵'''
    if self.row==0:
        return 'Matrix= \n "empty Matrix" \n'
    rt='Matrix=\n'
    for r in range(self.row):
      rt+="| "  
      for c in range(self.column-1):
        rt+=str(round(self[r+1, c+1],3))+', '
      rt+=str(round(self[r+1,self.column],3))+' |'
      rt+='\n'
    
    return rt      
      
  def __str__(self):
    '''打印矩阵'''
    return self.__repr__() 


def solve(A,b):
    return  A.invert()*b
    #invert(self):



      
if __name__ == '__main__':
# =============================================================================
#   m = Matrix(3,3,fill=2.0)
#   n = Matrix(3,3,fill=3.5)
#   m[1] = [1.,1.,2.]
#   m[2] = [1.,2.,1.]
#   m[3] = [2.,1.,1.]
#   p = m * n
#   q = m*2.1
#   r = m**3
#   #r.show()
#   #q.show()
#   #print(p[1,1])
#   #r = m.invert()
#   #s = r*m
#   print()
#   m.show()
#   print()
#   #r.show()
#   print()
#   #s.show()
#   print()
#   print(m.det())
#   
#   print(m)
# =============================================================================


    
    
# =============================================================================
# 
#     b=[[11,12,13,11],[4,5,6,1]]
#     #b=[[5,6],[7,8]]
#     a=[[1,2],[3,4]]
# 
#     A=Matrix()
#     A.fillwith(a)
#     
#     B=Matrix()
#     B.fillwith(b)
#     
#     AA=np.mat(a)
#     BB=np.mat(b)
# 
# =============================================================================

# =============================================================================
#     print(A)
#     print(A[2,2])
# 
#     print('detA=',A.det())
#     print('np det AA', nlg.det(AA))
# 
#     print("Matrix *\n",AA*BB)
#     print("nlg *\n",A*B)
#     print("AA**2:\n",AA**2)
#     print("A**2:\n",A**2)
# =============================================================================
    
# =============================================================================
#     N=4
#     mrand=[[random.randint(0,9) for i in range(N) ] for j in range(N)]
#   
#     #mrand=[[0, 2, 0],[3, 4, 5],[4, 8, 3]]
#     #X = np.random.randint(0, 5, [3, 2, 2])
#     
#     
#     MA=Matrix()
#     MA.fillwith(mrand)
#     MB=np.mat(mrand)
#     print(MA)
#     
#     t1=time.time()
#     inva=np.array(MA.invert()._matrix)
#     t2=time.time()
#     print("inva time", t2-t1)
#     
#     t1=time.time()
#     invb=np.array(MB.I)
#     t2=time.time()
#     print("numpy invb time", t2-t1)
#     
#     print("np nlg det:",nlg.det(MB))
#     print("matrix class det",MA.det())
#     print("matrix class det2",MA.det2())
#     
#     
#     ls=[[-2,-2,1],[-4,-8,4],[-1,5,0]]
#     m1=Matrix()
#     m1.fillwith(ls)
#     inv1=m1.invert()
#     
#     
#     m2=np.mat(np.array(ls))
#     inv2=m2.I
#     
# =============================================================================
    
    A=Matrix()
    b=Matrix()
    A.fillwith([[1,1,-1],[2,-3,4],[-3,1,-2]]) 
    b.fillwith([[-3],[23],[-15]])    
    print(solve(A,b))


  