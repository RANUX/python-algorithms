# -*- coding=utf-8 -*-
'''
Demonstrates minimum spanning tree with weighted graphs
'''
from graph import GraphW, TVertex
from heap import Heap


class Edge():

    def __init__(self, srcv, dstv, dist):
        self.srcv = srcv                 # index of a vertex starting edge
        self.dstv = dstv                 # index of a vertex ending edge
        self.dist = dist                 # distance from src to dest

    def __repr__(self):
        return "Edge({},{},{})".format(self.srcv, self.dstv, self.dist)

    def reprWithLabels(self, vertexList):
        return "Edge({},{},{})".format(vertexList[self.srcv], vertexList[self.dstv], self.dist)

class GraphMstw(GraphW):

    def __init__(self, maxVerts):
        super().__init__(maxVerts)
        self.nTree = 0                      # number of verts in tree
        self.pQueue = Heap(cmp=lambda e1,e2: e1.dist <= e2.dist)
        self.curVert = 0

    def addVertex(self, label):
        super().addVertex(label, TVertex)

    def mstw(self):
        ''' Minimum spanning tree '''
        self.curVert = 0

        while self.nTree < self.nv-1:                                # while not all verts in tree
            self.vertexList[self.curVert].isInTree = True            # put currentVert in tree
            self.nTree += 1

            for j in range(0, self.nv):
                if j == self.curVert:                                # skip if it's us
                    continue
                
                if self.vertexList[j].isInTree:                 # skip if in the tree
                    continue
                
                dist = self.adjMatrix[self.curVert][j]               # skip if no edge
                if dist == self.infinity:
                    continue

                self.putInPQueue(j, dist)                       # put it in PQ (maybe)
            
            if self.pQueue.isEmpty():
                print("Graph not connected")
                return
            
            edge = self.pQueue.pop()
            self.curVert = edge.dstv

            print( '{}{} '.format(self.vertexList[edge.srcv].label, self.vertexList[self.curVert].label) )
            
        
    def putInPQueue(self, newVert, newDist):
        oldEdge = self.pQueue.find(newVert, lambda e, v: e.dstv == v)

        if oldEdge:                           # is there another edge with the same destination vertex?
            if oldEdge.dist > newDist:
                self.pQueue.remove(oldEdge)
                newEdge = Edge( self.curVert, newVert, newDist)
                self.pQueue.add(newEdge)
            # else no action; just leave the old vertex there
        else:                              # no edge with same destination vertex
            edge = Edge( self.curVert, newVert, newDist)
            self.pQueue.add(edge)


def main():
    g = GraphMstw(6)
    g.addVertex('A')    # 0  (start for mst)
    g.addVertex('B')    # 1
    g.addVertex('C')    # 2
    g.addVertex('D')    # 3
    g.addVertex('E')    # 4
    g.addVertex('F')    # 5

    g.addEdge(0, 1, 6)  # AB  6
    g.addEdge(0, 3, 4)  # AD  4
    g.addEdge(1, 2, 10) # BC 10
    g.addEdge(1, 3, 7)  # BD  7
    g.addEdge(1, 4, 7)  # BE  7
    g.addEdge(2, 3, 8)  # CD  8
    g.addEdge(2, 4, 5)  # CE  5
    g.addEdge(2, 5, 6)  # CF  6
    g.addEdge(3, 4, 12) # DE 12
    g.addEdge(4, 5, 7)  # EF  7

    #g.showVertices()
    #g.showEdges()
    g.mstw()

if __name__ == '__main__':
    main()
