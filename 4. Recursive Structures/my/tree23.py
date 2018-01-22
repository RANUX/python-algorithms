# -*- coding=utf-8 -*-

class Node(object):

    def __init__(self):
        self.ORDER = 3
        self.numItems = 0
        self.items = [None]*(self.ORDER - 1)    # [None,None] index from 0-1
        self.children = [None]*self.ORDER       # [None,None,None] index from 0-2

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

