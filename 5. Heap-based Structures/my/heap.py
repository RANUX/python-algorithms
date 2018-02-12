
class Heap(object):
    def __init__(self, values = None, cmp=lambda a,b: a <= b):
        self.cmp = cmp
        if values is None:
            self.arr = []
        else:
            self.arr = list(values)
        self.n = len(self.arr)

        # takes O(n) to convert values into heap
        # create heap from array
        start = self.n//2 - 1           # only parent nodes with chilren
        for i in range(start, -1, -1):
            self.moveDown(i)


    def parent(self, i):
        """Get parent index of i-th index"""
        return (i-1)//2                     # i-1: indexing from 0, not from 1

    def left(self, i):
        """Get left child of i-th index"""
        return 2*i + 1

    def right(self, i):
        """Get right child of i-th index"""
        return 2*i + 2


    def isEmpty(self):
        """Determine if heap is empty."""
        return self.n == 0

    def pop(self):
        """Return smallest value and repair heap."""
        if self.n == 0:
            raise ValueError("Heap is empty")
        val = self.arr[0]
        self.n -= 1
        self.arr[0] = self.arr[self.n]
        self.moveDown(0)
        return val

    def __swap(self, a, b):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]

    def add(self, value):
        """Add value to heap and repair heap."""
        if self.n == len(self.arr):
            self.arr.append(value)
        else:
            self.arr[self.n] = value # reuse available space, because pop doesn't delete element

        i = self.n
        self.n += 1
        self.moveUp(i)

    def moveUp(self, i):
        parent = self.parent(i)
        bottomVal = self.arr[i]
        while i > 0 and self.cmp(self.arr[i], self.arr[parent]):
            self.arr[i] = self.arr[parent]
            i = parent
            parent = self.parent(i)

        self.arr[i] = bottomVal

    def moveDown(self, i):
        topVal = self.arr[i]

        while i < self.n//2:                # while node has at least one child
            left = self.left(i)
            right = left + 1

            if right < self.n and not self.cmp(self.arr[left], self.arr[right]):
                largeChild = right
            else:
                largeChild = left

            if self.cmp(topVal, self.arr[largeChild]):
                break

            self.arr[i] = self.arr[largeChild]
            i = largeChild

        self.arr[i] = topVal

    def heapifyRec(self, index):
        """ From list to heap"""
        if index > self.n//2-1:   # if node without children
            return
        self.heapifyRec(index*2+2) # right subtree to heap
        self.heapifyRec(index*2+1) # left subtree to heap
        self.moveDown(index)

    def __len__(self):
        return self.n

    def __repr__(self):
        """Return representation of heap as array."""
        return 'heap:[' + ','.join(map(str, self.arr[:self.n])) + ']'
