from graph import GraphWD, TVertex

class DistParent():
    def __init__(self, pv, dst):
        self.distance = dst
        self.parentVert = pv

class SPWGraph(GraphWD):
    ''' Demonstrates shortest path with weighted, directed graphs '''
    def __init__(self, maxVerts):
        super().__init__(maxVerts)
        self.nTree = 0                                      # number of verts in tree
        self.sPaths = [None]*maxVerts                       # array for shortest-path data
        self.currentVert = 0                                # current vert index
        self.distStartToCurrent = 0                         # distance from startVert to currentVert

    def addVertex(self, label):
        super().addVertex(label, TVertex)

    def findShortPaths(self, startVertex=0):
        ''' Find all shortest paths from startVertex to others '''
        self.vertexList[startVertex].isInTree = True
        self.nTree = 1                                      # put start vertex in tree
        self.initShortPathsTable(startVertex)
        
        while self.nTree < self.nv:                         # until all vertices are in the tree
            indexMin = self.getMin()                        # get min dist vert index from sPaths
            minDist  = self.sPaths[indexMin].distance

            if minDist == self.infinity:
                print('There are unreachable vertices')
                break
            else:
                self.currentVert = indexMin
                self.distStartToCurrent = minDist
            
            self.vertexList[self.currentVert].isInTree = True   # put current vertex in tree
            self.nTree += 1
            self.adjustSPath()                              # update sPath[] array
    
    def initShortPathsTable(self, startVertex):
        for j in range(0, self.nv):                         # transfer row of distances from adjMat to sPaths
            tmpDist = self.adjMatrix[startVertex][j]
            self.sPaths[j] = DistParent(startVertex, tmpDist)

    def getMin(self):
        ''' Get index of min dist adjecent unvisited vertex from sPath '''
        minDist = self.infinity
        indexMin = 0
        for j in range(1, self.nv):
            if not self.vertexList[j].isInTree and self.sPaths[j].distance < minDist:
                minDist = self.sPaths[j].distance
                indexMin = j

        return indexMin

    def adjustSPath(self):
        ''' Adjust values in shortest-path array sPath '''
        col = 1
        while col < self.nv:
            if self.vertexList[col].isInTree:               # if this column's vertex already in tree, skip it
                col += 1
                continue

            currToAdjEdgeDist  = self.adjMatrix[self.currentVert][col]
            startToAdjEdgeDist = self.distStartToCurrent + currToAdjEdgeDist
            currSPathDist = self.sPaths[col].distance

            if startToAdjEdgeDist < currSPathDist:                      # compare distance from start with sPath entry
                self.sPaths[col].parentVert = self.currentVert          # if shorter, update sPaths value
                self.sPaths[col].distance = startToAdjEdgeDist
                
            col += 1

    def showShortPaths(self):
        outs = ''
        for j in range(0, self.nv):
            outs += '{}='.format(self.vertexList[j].label)
            if self.sPaths[j].distance == self.infinity:
                outs += 'inf'
            else:
                outs += '{}'.format(self.sPaths[j].distance)
            outs += '({}) '.format(self.vertexList[ self.sPaths[j].parentVert ].label)
        print(outs)


def main():
    g = SPWGraph(5)
    g.addVertex('A')     # 0  (start)
    g.addVertex('B')     # 1
    g.addVertex('C')     # 2
    g.addVertex('D')     # 3
    g.addVertex('E')     # 4

    # g.showVertices()

    g.addEdge(0, 1, 50)  # AB 50
    g.addEdge(0, 3, 80)  # AD 80
    g.addEdge(1, 2, 60)  # BC 60
    g.addEdge(1, 3, 90)  # BD 90
    g.addEdge(2, 4, 40)  # CE 40
    g.addEdge(3, 2, 20)  # DC 20
    g.addEdge(3, 4, 70)  # DE 70
    g.addEdge(4, 1, 50)  # EB 50

    # g.showEdges()

    g.findShortPaths(0)
    g.showShortPaths()

    am = g.shortesPaths()
    print(am)


if __name__ == "__main__":
    main()