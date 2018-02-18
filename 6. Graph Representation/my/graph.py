from stack import Stack
from queue import Queue
from functools import reduce

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

    def __repr__(self):
        return "{}:{}".format(self.label, self.visited)

class BaseGraph:
    def __init__(self, maxVerts, fillAdjVal=0):
        self.maxVerts = maxVerts
        self.vertexList = []
        self.adjMatrix = []    # adjacent matrix
        self.nv = 0           # number of vertices
        for i in range(0, self.maxVerts):
            self.adjMatrix.append([fillAdjVal]*self.maxVerts)

    def addVertex(self, label, vtype=Vertex):
        self.vertexList.append(vtype(label))

        self.nv += 1
    

    def showVertex(self, *vs):
        print(list(reduce(lambda p, v: p+[self.vertexList[v]], vs, [])))

    def showVertices(self):
        print(self.vertexList)

    def showEdges(self):
        for i in range(0, self.maxVerts):
            print(self.adjMatrix[i])

    def getAdjUnvisitedVertex(self, v):
        for j in range(0, self.nv):
            if self.adjMatrix[v][j] == 1 and self.vertexList[j].visited == False:
                return j
        return -1

    def noSuccessors(self):
        ''' Returns vert with no successors '''
        for row in range(0, self.nv):
            isEdge = False
            for col in range(0, self.nv):
                if self.adjMatrix[row][col] > 0:
                    isEdge = True
                    break

            if not isEdge:
                return row

        return -1

    def removeVertex(self, v):
        if v != self.nv-1:                                  # if not last vertex
            for j in range(v, self.nv-1):                   # remove from vertex list
                self.vertexList[j] = self.vertexList[j+1]

            for row in range(v, self.nv-1):                 # remove row from adj matrix
                self.moveRowUp(row, self.nv)
            for col in range(v, self.nv-1):                 # remove col from adj matrix
                self.moveColLeft(col, self.nv-1)

        self.nv -= 1                                        # one less vertex

    def moveRowUp(self, row, length):
        for col in range(0, length):
            self.adjMatrix[row][col] = self.adjMatrix[row+1][col]

    def moveColLeft(self, col, length):
        for row in range(0, length):
            self.adjMatrix[row][col] = self.adjMatrix[row][col+1]



class DirectedGraph(BaseGraph):

    def __init__(self, maxVerts):
        BaseGraph.__init__(self, maxVerts)
        self.sortedVerts = [None]*maxVerts
        self.nvOrig = 0

    def addEdge(self, start, end):
        self.adjMatrix[start][end] = 1

    def sortTopo(self):
        '''Topological sort'''
        self.nvOrig = self.nv

        while self.nv > 0:
            curVert = self.noSuccessors()

            if curVert == -1:
                print("ERROR: Graph has cycles")
                return

            self.sortedVerts[self.nv-1] = self.vertexList[curVert]
            self.removeVertex(curVert)

    def showTopoSortedVerts(self):
        if self.nv != self.nvOrig:
            result = ''
            for i in range(0, self.nvOrig):
                result += self.sortedVerts[i].label + ' '
            print(result)


class Graph(BaseGraph):

    def __init__(self, maxVerts):
        BaseGraph.__init__(self, maxVerts)

    def addEdge(self, start, end):
        self.adjMatrix[start][end] = 1
        self.adjMatrix[end][start] = 1

class GraphW(BaseGraph):
    ''' Weighted graph '''

    def __init__(self, maxVerts, infinity=10000):
        self.infinity = infinity
        BaseGraph.__init__(self, maxVerts, self.infinity)

    def addEdge(self, start, end, weight):
        self.adjMatrix[start][end] = weight
        self.adjMatrix[end][start] = weight


class BFSGraph(Graph):

    def __init__(self, maxVerts):
        Graph.__init__(self, maxVerts)
        self.queue = Queue()

    def bfs(self):
        self.vertexList[0].visited = True
        self.showVertex(0)
        self.queue.put(0)

        while not self.queue.empty():
            #print(self.queue)
            v1 = self.queue.get()
            v2 = self.getAdjUnvisitedVertex(v1)

            while v2 != -1:
                self.vertexList[v2].visited = True
                self.showVertex(v2)
                self.queue.put(v2)
                v2 = self.getAdjUnvisitedVertex(v1)

        # empty stack, job done, reset vert flags
        for j in range(0, self.nv):
            self.vertexList[j].visited = False


class DFSGraph(Graph):
    
    def __init__(self, maxVerts):
        Graph.__init__(self, maxVerts)
        self.stack = Stack()

    def dfs(self):
        self.vertexList[0].visited = True
        self.showVertex(0)
        self.stack.push(0)

        while not self.stack.isEmpty():
            #print(self.stack)
            cv = self.stack.peek()               # current vertex
            v = self.getAdjUnvisitedVertex( cv )
            if v == -1:
                self.stack.pop()
            else:
                self.vertexList[v].visited = True
                self.stack.push(v)
                self.showVertex(cv,v)           # show mst tree

        # empty stack, job done, reset vert flags
        for j in range(0, self.nv):
            self.vertexList[j].visited = False

def testDFS():
    g = DFSGraph(6)
    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')
    g.addVertex('G')

    print(g.showVertices())

    g.addEdge(0, 1) # AB
    g.addEdge(0, 2) # AC
    g.addEdge(0, 3) # AD
    g.addEdge(0, 4) # AE
    g.addEdge(1, 2) # BC
    g.addEdge(1, 3) # BD
    g.addEdge(1, 4) # BE
    g.addEdge(2, 3) # CD
    g.addEdge(2, 4) # CE
    g.addEdge(3, 4) # DE

    print(g.showEdges())

    print("visits:")
    g.dfs()

def testBFS():
    g = BFSGraph(6)
    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')
    g.addVertex('G')

    print(g.showVertices())

    g.addEdge(0, 1) # AB
    g.addEdge(1, 2) # BC
    g.addEdge(1, 5) # BG
    g.addEdge(0, 3) # AD
    g.addEdge(3, 4) # DE

    print(g.showEdges())

    print("visits:")
    g.bfs()

def testTopoSortGraph():
    g = DirectedGraph(8)
    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')
    g.addVertex('F')
    g.addVertex('G')
    g.addVertex('H')

    g.addEdge(0, 3)     # AD
    g.addEdge(0, 4)     # AE
    g.addEdge(1, 4)     # BE
    g.addEdge(2, 5)     # CF
    g.addEdge(3, 6)     # DG
    g.addEdge(4, 6)     # EG
    g.addEdge(5, 7)     # FH
    g.addEdge(6, 7)     # GH

    g.sortTopo()
    g.showTopoSortedVerts()

def main():
    #testDFS()
    #testBFS()
    testTopoSortGraph()



if __name__ == "__main__":
    main()