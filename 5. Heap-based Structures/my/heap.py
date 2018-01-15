
class Heap(object):
    def __init__(self, values = None, cmp=lambda a,b: a < b):
        self.cmp = cmp
        if values is None:
            self.arr = []
        else:
            self.arr = list(values)
        self.n = len(self.arr)

        # takes O(n) to convert values into heap
        start = self.n//2 - 1           # only parent nodes with chilren
        for i in range(start, -1, -1):
            self.heapify (i)


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
        self.heapify(0)
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

        while i > 0:
            parent = self.parent(i)
            if self.cmp(self.arr[i], self.arr[parent]):
                self.__swap(i, parent)
                i = parent
            else:
                break


    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)

        smallest = i

        # Find smallest element of A[i], A[left], and A[right]
        if left < self.n and self.cmp(self.arr[left], self.arr[i]):
            smallest = left

        if right < self.n and self.cmp(self.arr[right], self.arr[smallest]):
            smallest = right

        # If smallest is not already the parent then swap and propagate
        if smallest != i:
            self.__swap(i, smallest)
            self.heapify(smallest)

    def __len__(self):
        return self.n

    def __repr__(self):
        """Return representation of heap as array."""
        return 'heap:[' + ','.join(map(str, self.arr[:self.n])) + ']'
