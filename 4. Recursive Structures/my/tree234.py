# -*- coding=utf-8 -*-

class Node(object):

    def __init__(self):
        self.ORDER = 4
        self.numItems = 0
        self.items = [None]*(self.ORDER - 1)    # [None,None,None] index from 0-2
        self.children = [None]*self.ORDER       # [None,None,None,None] index from 0-3


    def connectChild(self, childNum, child):
        """ Connect child to this node """
        self.children[childNum] = child

        if child != None:
            child.parent = self

    def disconnectChild(self, childNum):
        """ Disconnect child from this node, return it """
        tempNode = self.children[childNum]
        self.children[childNum] = None
        return tempNode

    def getChild(self, childNum):
        """ Get child node """
        return self.children[childNum]

    def isLeaf(self):
        """ Is node leaf """
        return True if (self.children[0] == None) else False

    def getNumItems(self):
        """ Get number of items """
        return self.numItems

    def getItem(self, index):
        """ Get item """
        #  get DataItem at index
        return self.items[index]

    def isFull(self):
        """ Check if items array full """
        return True if (self.numItems == self.ORDER - 1) else False

    def findItem(self, key):
        """ Find item by key. Return index of item (within node) """
        j = 0
        while j < self.ORDER - 1:
            #  if found,
            #  otherwise,
            if self.items[j] == None:
                break                           # return -1
            elif self.items[j] == key:
                return j
            j += 1
        return -1

    def insertItem(self, newItem):
        """ Insert new item """
        self.numItems += 1
        
        for j in range(self.ORDER-2, -1, -1):           # shift items
            if self.items[j] == None:
                continue
            else:
                if newItem < self.items[j]:
                    self.items[j + 1] = self.items[j]   # shift right bigger
                else:
                    self.items[j + 1] = newItem         # insert new item
                    return j + 1                        # return index to newItem

        self.items[0] = newItem
        return 0

    def removeItem(self):
        """ Remove item """
        temp = self.items[self.numItems - 1]
        self.items[self.numItems - 1] = None
        self.numItems -= 1
        return temp

    def inorder(self):
        j = 0
        while j < self.numItems:
            if self.children[j] != None:
                yield from self.children[j].inorder()
            yield self.items[j]
            j += 1

        if self.children[j] != None:
            yield from self.children[j].inorder()


    def __repr__(self):
        """Useful debugging function to produce linear tree representation."""
        return "{}:{}".format(self.items, self.children)

class Tree234(object):

    def __init__(self, *initVals):
        self.root = Node()
        for _ in initVals:
            self.insert(_)

    def find(self, key):
        """ Find item """
        curNode = self.root
        childNum = 0

        while True:
            childNum = curNode.findItem(key)
            if childNum != -1:
                return childNum
            elif curNode.isLeaf():
                return -1
            else:
                curNode = self.getNextChild(curNode, key)

    def insert(self, value):
        """ Insert new value """
        node = self.root

        while True:
            if node.isFull():
                self.split(node)
                node = node.parent
                node = self.getNextChild(node, value)
            elif node.isLeaf():
                break
            else:
                node = self.getNextChild(node, value)

        node.insertItem(value)

    def split(self, thisNode):
        """ Split the node """
        itemIndex = 0

        itemC = thisNode.removeItem()
        itemB = thisNode.removeItem()
        child2 = thisNode.disconnectChild(2)
        child3 = thisNode.disconnectChild(3)
        
        if thisNode == self.root:
            self.root = Node()
            parent = self.root
            self.root.connectChild(0, thisNode)
        else:
            parent = thisNode.parent

        itemIndex = parent.insertItem(itemB)
        j = parent.numItems - 1
        while j > itemIndex:                    # shift children to right for new child
            temp = parent.disconnectChild(j)
            parent.connectChild(j + 1, temp)
            j -= 1

        newRight = Node()
        parent.connectChild(itemIndex + 1, newRight)
        newRight.insertItem(itemC)
        newRight.connectChild(0, child2)        # connect 2,3 childrens to rightNode
        newRight.connectChild(1, child3)

    def getNextChild(self, node, value):
        """ Get next child """
        j = 0
        while j < node.numItems:
            if value < node.getItem(j):
                return node.getChild(j)
            j += 1

        return node.getChild(j)

    def __iter__(self):
        """In order traversal of elements in the tree."""
        if self.root:
            for e in self.root.inorder():
                yield e

    def displayTree(self):
        """ Display tree """
        self.recDisplayTree(self.root, 0, 0)

    def recDisplayTree(self, node, level, childNumber):
        """ Recursevly display tree """
        print("level={} child={} {}".format(level, childNumber, node))

        for j in range(0, node.numItems+1):
            nextNode = node.getChild(j)
            if nextNode != None:
                self.recDisplayTree(nextNode, level + 1, j)
            else:
                return


if __name__ == "__main__":
    t=Tree234(30, 50, 70, 40, 20, 80, 25, 90, 75, 10)
    #t.displayTree()
    for v in t:
        print(v)