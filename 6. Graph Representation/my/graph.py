from stack import Stack
from queue import Queue

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

    def __repr__(self):
        return "{}:{}".format(self.label, self.visited)

class BaseGraph:

    def __init__(self, maxVerts):
        self.maxVerts = maxVerts
        self.vertexList = []
        self.adjacent = []    # adjacent matrix
        self.nv = 0           # number of vertices
        for i in range(0, self.maxVerts):
            self.adjacent.append([0]*self.maxVerts)

    def addVertex(self, char):
        self.vertexList.append(Vertex(char))
        self.nv += 1

    def addEdge(self, start, end):
        self.adjacent[start][end] = 1
        self.adjacent[end][start] = 1

    def showVertex(self, v):
        print(self.vertexList[v])

    def showVertices(self):
        print(self.vertexList)

    def showEdges(self):
        for i in range(0, self.maxVerts):
            print(self.adjacent[i])

    def getAdjUnvisitedVertex(self, v):
        for j in range(0, self.nv):
            if self.adjacent[v][j] == 1 and self.vertexList[j].visited == False:
                return j
        return -1


class BFSGraph(BaseGraph):

    def __init__(self, maxVerts):
        BaseGraph.__init__(self, maxVerts)
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


class DFSGraph(BaseGraph):
    
    def __init__(self, maxVerts):
        BaseGraph.__init__(self, maxVerts)
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
                self.showVertex(v)

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
    g.addEdge(1, 2) # BC
    g.addEdge(1, 5) # BG
    g.addEdge(0, 3) # AD
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

def main():
    #testDFS()
    testBFS()



if __name__ == "__main__":
    main()