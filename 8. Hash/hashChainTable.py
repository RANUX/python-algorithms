from sortedLinkedList import SortedLinkedList

class HashChainTable(object):

    def __init__(self, size):
        self.hashArray = []
        self.size = size
        for i in range(0, size):
            self.hashArray.append(SortedLinkedList())

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        """ Insert key  """
        hashVal = self.hash(key)
        self.hashArray[hashVal].insert(key)

    def delete(self, key):
        hashVal = self.hash(key)
        self.hashArray[hashVal].remove(key)

    def find(self, key):
        """ Find value by key """
        hashVal = self.hash(key)
        return self.hashArray[hashVal].find(key)

    def __str__(self):
        s = ''
        for i, item in enumerate(self.hashArray):
            s = '{}{} {}\n'.format(s, i, str(item))
        return s

if __name__ == "__main__":
    ht = HashChainTable(10)
    data = [1, 38, 37, 16, 20, 3, 11, 24, 5, 16, 10, 31, 18, 12, 30, 1, 19, 36, 41, 15, 25]
    for e in data:
        ht.insert(e)
    print(ht)
    print(ht.find(1))