#!/usr/bin/env python
#Copyright 2008, Angel Yanguas-Gil

__all__ = ['Dcel', 'Vertex', 'Hedge', 'Face']

#from xygraph import Xygraph

'''
https://www.desmos.com/calculator/ejatebvup4

http://www.eecs.tufts.edu/~vporok01/c163/#

http://paperjs.org/examples/voronoi/

ahttps://www.cs.hmc.edu/~mbrubeck/voronoi.html

https://www.boost.org/doc/libs/1_54_0/libs/polygon/doc/voronoi_main.htm

http://blog.ivank.net/fortunes-algorithm-and-implementation.html

https://demonstrations.wolfram.com/FortunesAlgorithmForVoronoiDiagrams/

https://gamedevelopment.tutsplus.com/tutorials/how-to-use-voronoi-diagrams-to-control-ai--gamedev-11778

https://en.wikipedia.org/wiki/Circumscribed_circle#Circumscribed_circles_of_triangles

http://geomalgorithms.com/index.html

'''

import math as m

class DcelError(Exception): pass

class Vertex: # V图的顶点类
    """Minimal implementation of a vertex of a 2D dcel"""

    def __init__(self, px, py,id=0):
        self.id=id  #顶点的id
        self.x = px #顶点的x左边
        self.y = py #顶点的y左边
        self.IncidentEdge = None  #顶点的关联第一个出边 outgoing half edges
        self.hedgelist = []    #顶点所有关联出边列表，
 
    def sortincident(self):
        #调用key=hsort 函数（按照ccw逆时针角度大小对顶点关联的边进行逆排序）
        self.hedgelist.sort(hsort, reverse=True)


class Hedge:#V图的half edge半边类
    """Minimal implementation of a half-edge of a 2D dcel"""

    def __init__(self,v1=None,v2=None,id=None):
        #The origin is defined as the vertex it points to
        self.id=id
        self.origin = v2  #half edge 的起点
        self.twin = None #孪生的另一个半边
        self.face = None #边关联的面(左侧面)
        self.nexthedge = None #后继半边half edge
        #self.angle = hangle(v2.x-v1.x, v2.y-v1.y)
        self.prevhedge = None #前驱half edge
        #self.length = m.sqrt((v2.x-v1.x)**2 + (v2.y-v1.y)**2)


class Face: # V图面的类
    """Implements a face of a 2D dcel"""

    def __init__(self,id=None):
        self.id=id
        self.wedge = None   #面关联的半边（面在有向半边的左侧）
        self.data = None
        self.external = None

    def area(self): # face的面积
        h = self.wedge
        a = 0
        #is 操作符是Python语言的一个内建的操作符。
        #它的作用在于比较两个变量是否指向了同一个对象
        #is是比较两个引用是否指向了同一个对象（引用比较,比较的是内存地址,id是否相同）
        #==是比较两个对象是否相等
        #https://blog.csdn.net/liweiblog/article/details/53198479
        while(not h.nexthedge is self.wedge): 
            p1 = h.origin
            p2 = h.nexthedge.origin
            a += p1.x*p2.y - p2.x*p1.y
            h = h.nexthedge

        p1 = h.origin
        p2 = self.wedge.origin
        a = (a + p1.x*p2.y - p2.x*p1.y)/2
        return a

    def perimeter(self): #面的周长
        h = self.wedge
        p = 0
        while (not h.nexthedge is self.wedge):
            p += h.length
            h = h.nexthedge
        return p

    def vertexlist(self): #与面关联的顶点的列表
        h = self.wedge 
        pl = [h.origin]
        while(not h.nexthedge is self.wedge):
            h = h.nexthedge
            pl.append(h.origin)
        return pl

    def isinside(self, p): #点p是否在面内
        """Determines whether a point is inside a face"""

        h = self.wedge
        inside = False
        if lefton(h, p): #凸多边形可以用左手判断 ， 非凸多边形可以用The Crossing Number 判断
            while(not h.nexthedge is self.wedge):
                h = h.nexthedge
                if not lefton(h, p):
                    return False
            return True
        else:
            return False


class Dcel():
    """
    Implements a doubly-connected edge list
    """

    def __init__(self, vl=[], el=[], clip=None):
        #Xygraph.__init__(self, vl, el)
        self.vertices = []  #顶点列表
        self.hedges = []   #边列表
        self.faces = []   #面列表
        if vl != []:
            if clip is not None:
                self.clip(clip)
            self.build_dcel()  #顶点非空，则开始dcel数据结构的构建函数
 

    def build_dcel(self): # 通过顶点和边列表构建dcel数据结构
        """
        Creates the dcel from the list of vertices and edges
        """
 
#Step 1: vertex list creation
        for v in self.vl:
            self.vertices.append(Vertex(v[0], v[1])) #v[0],v[1], x,y 坐标

#Step 2: hedge list creation. Assignment of twins and
#vertices
        for e in self.el:
            if e[0] >= 0 and e[1] >= 0: # e包含[e[0],e[1]] ，e[0],e[1]为两个顶点的索引序号 
                h1 = Hedge(self.vertices[e[0]], self.vertices[e[1]]) #用两个点初始化half edge
                h2 = Hedge(self.vertices[e[1]], self.vertices[e[0]])
                h1.twin = h2
                h2.twin = h1
                self.vertices[e[1]].hedgelist.append(h1)
                self.vertices[e[0]].hedgelist.append(h2)
                self.hedges.append(h2)
                self.hedges.append(h1)

        #Step 3: Identification of next and prev hedges,构建前驱后继有向边 
        for v in self.vertices:
            v.sortincident() # 顶点V关联的边V.hedgelist按照顺时针排序（ccw角度逆时针逆序排序 ）
            l = len(v.hedgelist)
            if l < 2:
                raise DcelError(
                    "Badly formed dcel: less than two hedges in vertex")
            else:
                for i in range(l-1):  #关联的是边右侧面？ 
                    v.hedgelist[i].nexthedge = v.hedgelist[i+1].twin
                    v.hedgelist[i+1].prevhedge = v.hedgelist[i]
                v.hedgelist[l-1].nexthedge = v.hedgelist[0].twin
                v.hedgelist[0].prevhedge = v.hedgelist[l-1]

        #Step 4: Face assignment 面与有向边的关联 
        provlist = self.hedges[:]
        nf = 0
        nh = len(self.hedges)

        while nh > 0:
            h = provlist.pop()
            nh -= 1
            #We check if the hedge already points to a face
            if h.face == None:
                f = Face()
                nf += 1
                #We link the hedge to the new face
                f.wedge = h
                f.wedge.face = f
                #And we traverse the boundary of the new face
                while (not h.nexthedge is f.wedge):
                    h = h.nexthedge
                    h.face = f
                self.faces.append(f)
                
        #And finally we have to determine the external face 
        for f in self.faces:
            f.external = f.area() < 0


    def findpoints(self, pl, onetoone=False): # 给定一系列点，返回包含点的面
        """Given a list of points pl, returns a list of
        with the corresponding face each point belongs to and
        None if it is outside the map.

        """
        ans = []
        if onetoone:
            fl = self.faces[:]
            for p in pl:
                found = False
                for f in fl:
                    if f.external:
                        continue
                    if f.isinside(p):
                        fl.remove(f)
                        found = True
                        ans.append(f)
                        break
                if not found:
                    ans.append(None)

        else:
            for p in pl:
                found = False
                for f in self.faces:
                    if f.external:
                        continue
                    if f.isinside(p):
                        found = True
                        ans.append(f)
                        break
                if not found:
                    ans.append(None)

        return ans

    def load(self, filename): #从文件中开始读取点和边的信息 
        """reads a dcel from file using xygraph file format"""
        a = Xygraph.load(self, filename)
        self.build_dcel()
        return a

    def areas(self):
        return [f.area() for f in self.faces if not f.external]

    def perimeters(self):
        return [f.perimeter() for f in self.faces if not f.external]

    def nfaces(self):
        return len(self.faces)

    def nvertices(self):
        return len(self.vertices)

    def nedges(self):
        return len(self.hedges)/2

    def minmax(self):
        """Determines the boundary box of the vertices in the graph"""
        vx = [v[0] for v in self.vl]
        vy = [v[1] for v in self.vl]
        self.xmax, self.xmin = max(vx), min(vx)
        self.ymax, self.ymin = max(vy), min(vy)


#Misc. functions


def hsort(h1, h2):# 按照ccw逆时针方向的角度大小比较两个半边
    """Sorts two half edges counterclockwise"""

    if h1.angle < h2.angle:
        return -1
    elif h1.angle > h2.angle:
        return 1
    else:
        return 0


def checkhedges(hl): #检验前驱，后续有向边的整体一致性 
    """Consistency check of a hedge list: nexthedge, prevhedge"""

    for h in hl:
        if h.nexthedge not in hl or h.prevhedge not in hl:
            raise DcelError("Problems with an orphan hedge...")


def area2(hedge, point): #边和边外一点构成的三角形的面积： 两个向量的叉积/2 
    """Determines the area of the triangle formed by a hedge and
    an external point"""

    pa = hedge.twin.origin
    pb=hedge.origin
    pc=point
    return (pb.x - pa.x)*(pc[1] - pa.y) - (pc[0] - pa.x)*(pb.y - pa.y)


def lefton(hedge, point): # 点是否在边的左边 
    """Determines if a point is to the left of a hedge"""

    return area2(hedge, point) >= 0


def hangle(dx,dy): #边相对于x轴的的角度
    """Determines the angle with respect to the x axis of a segment
    of coordinates dx and dy
    """

    l = m.sqrt(dx*dx + dy*dy)
    if dy > 0:
        return m.acos(dx/l)
    else:
        return 2*m.pi - m.acos(dx/l)


if __name__=='__main__':
    import sys
    d = Dcel()
    d.load(sys.argv[1])
    for a,p in zip(d.areas(), d.perimeters()):
        print(a,p)


