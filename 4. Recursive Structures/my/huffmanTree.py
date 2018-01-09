import sys
sys.path.append('../../../')
from utils import _build_tree_string
from collections import Counter
from priorityQueue import PriorityQueue

class BinaryNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    @property
    def value(self):
        return '{}:{}'.format(self.char, self.frequency)

    def __str__(self):
        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.root = None
        self.encTable = {}
        self.decTable = {}
        self.buildTree(text)
        self.encodeTable(self.root, '')

    def buildTree(self, text):
        queue = PriorityQueue(cmp=lambda a,b: a.frequency > b.frequency)
        for v,f in dict(Counter(list(text))).items():
            queue.enqueue(BinaryNode(v, f))

        while queue.size() > 1:
            nodeL = queue.dequeue()
            nodeR = queue.dequeue()
            parent = BinaryNode(None, nodeL.frequency+nodeR.frequency)
            parent.left = nodeL
            parent.right = nodeR
            queue.enqueue(parent)

        self.root = queue.dequeue()

    def encodeTable(self, node, code):
        if node:
            if node.char != None:
                self.encTable[node.char] = code
                self.decTable[code] = node.char
            self.encodeTable(node.left, code+'0')
            self.encodeTable(node.right, code+'1')

    def encode(self, text):
        return ''.join([self.encTable[ch] for ch in text])

    def decode(self, binary):
        sequence = ''
        s = ''
        for b in binary:
            sequence += b
            decoded = self.decTable.get(sequence)
            if decoded:
                s += decoded
                sequence = ''

        return s

if __name__ == "__main__":
    text = "SUSIE SAYS IT IS EASY"
    ht = HuffmanTree(text)
    print(ht.root)
    print(ht.encTable)
    encText = ht.encode(text)
    print("Encode:",encText)
    print("Decode:",ht.decode(encText))
