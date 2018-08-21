# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 08:38:41 2018

@author: zhouliang
"""

#import cv3
#import os  
import numpy as np
from PIL import Image  
import matplotlib.pyplot as plt  
#from scipy.misc import imread, imresize
#from scipy import signal
#import pylab
#from scipy import misc


'''
整数方法：Gray=(R*30+G*59+B*11)/100
'''
def img_int_gray(arr):
    rgb_weight =np.array([0.2125, 0.7154, 0.0721]) # RGB--取灰度比例
    gray_arr=np.dot(arr,rgb_weight)     #矩阵和np数组的点积broadcast广播
# =============================================================================
#     gray_arr=np.zeros((len(arr),len(arr)))
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             gray_arr[i][j]=arr[i][j][0]*0.2125+arr[i][j][1]*0.7154+arr[i][j][2]*0.0721
# =============================================================================
    return gray_arr

def trans_inv(trans_matrix,img=grayimg):
    fig=plt.figure()            
    newimg=np.ones((nrow,ncol),dtype='uint8')*255

    for i in range(0,nrow):
        for j in range(0,ncol):
            point=np.matrix([i,j])
            #newpoint=point.dot(inv_rotate)
            #newpoint=point.dot(inv_shear)
            newpoint=point.dot(trans_matrix)
    
            x=int(newpoint[0,0])
            y=int(newpoint[0,1])
            if 0<x<nrow:
                if 0<y<ncol:
                    newimg[i,j]=img[x,y]
                    
                    
    ax = fig.add_subplot(111)   #第4个子图
    ax.imshow(newimg,cmap=plt.cm.gray)
    plt.show()


def trans(trans_matrix,img=grayimg):
    fig=plt.figure()            
    newimg=np.ones((nrow,ncol),dtype='uint8')*255
    #newimg=np.zeros((nrow,ncol))
    

    for i in range(nrow):
        for j in range(ncol):
            point=np.matrix([i,j])
            #newpoint=point.dot(rotate)
            #newpoint=point.dot(shear)
            newpoint=point.dot(trans_matrix)
            
            x=int(newpoint[0,0])
            y=int(newpoint[0,1])
            if 0<x<nrow:
                if 0<y<ncol:
                    newimg[x,y]=img[i,j]
                    
    ax = fig.add_subplot(111)   #第5个子图
    ax.imshow(newimg,cmap=plt.cm.gray)
    plt.show()

            
def imgcoor(nrow,ncol): #生成一个坐标系统
    mcoor=np.zeros((nrow,ncol,2)) 
    for i in range(nrow):
        for j in range(ncol):
            mcoor[i,j,0]=i
            mcoor[i,j,1]=j
    return mcoor


fig=plt.figure()            

# =============================================================================
# ax = fig.add_subplot(211)
# img1= np.array(Image.open("D:/bg2.jpg"),dtype='uint8')
# ax.imshow(img1)  #默认配置
# =============================================================================


img2= np.array(Image.open("D:/bg24.bmp"),dtype='uint8')

fig=plt.figure()            
ax = fig.add_subplot(111)   #第 个子图
ax.imshow(img2)
plt.show()

grayimg=img_int_gray(img2)
nrow=grayimg.shape[0]
ncol=grayimg.shape[1]

fig=plt.figure() 
ax = fig.add_subplot(111)   #第 个子图
ax.imshow(grayimg, cmap=plt.cm.gray)
plt.show()

#waitKey()
theta =np.pi/(-6)
scalex=1.5
scaley=1.5
shearx=0.1
sheary=0.4
m_shear=np.matrix([[1, shearx],[sheary, 1]])
m_rotate=np.matrix([[np.cos(theta),-1*np.sin(theta)],[np.sin(theta),np.cos(theta)]])
m_scale=np.matrix([[scalex,0],[0,scaley]])
inv_rotate=m_rotate.I
inv_shear=m_shear.I
inv_scale=m_scale.I


#trans_inv(inv_rotate)
trans_inv(inv_shear)
#trans_inv(inv_scale)








#m_coord=imgcoor(nrow,col)



'''

 
height, width = img.shape[:2]
res2 = cv3.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow('res2', res2)
 
cv2.waitKey(0)

#X = np.random.randint(0, 5, [3, 2, 2])
g = np.zeros((2, 2, 3), dtype=np.uint8)
g.shape                    # (2, 2, 3)
h = g.astype(np.float)  # 用另一种类型表示

l = np.arange(10)      	# 类似range，array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
m = np.linspace(0, 6, 5)# 等差数列，0到6之间5个取值，array([ 0., 1.5, 3., 4.5, 6.])

a = np.arange(24).reshape((2, 3, 4))
np.save('p.npy', p)     # 保存到文件
q = np.load('p.npy')    # 从文件读取
np.loadtxt(FILENAME, dtype=int, delimiter=' ')
np.savetxt("a.txt", a, fmt="%d", delimiter=",")


g = np.split(np.arange(9), 3)
'''