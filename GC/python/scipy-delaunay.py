# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:56:33 2018

@author: user
"""

from scipy.spatial import Voronoi
from scipy.spatial import KDTree

import numpy as np

points  = np.array([[0, 0],[0, 1],[0, 2],
                    [1, 0],[1, 1],[1, 2],
                    [2, 0],[2, 1],[2, 2]])
vor = Voronoi(points)

print(vor.vertices)

print(vor.regions )
       #Indices of the *Voronoi vertices* forming each Voronoi region. 
                       #-1 indicates vertex outside the Voronoi diagram.

vor.ridge_vertices     
# 12条
# Indices of the Voronoi vertices forming each Voronoi ridge.

vor.ridge_points      
#Indices of the points between which each Voronoi ridge lies.


tree = KDTree(points)
print( tree.query([0.1, 0.1]) )       #哪个点距离这个点最近
    #(0.14142135623730953, 0)
    