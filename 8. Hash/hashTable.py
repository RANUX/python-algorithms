
class HashTable(object):
    REMOVED_KEY = -1

    def __init__(self, size):
        """ Size should be prime number for check all array cells. 
            If many keys have common divider with size, they will group in same position
        """
        if not self.isPrime(size):
            size = self.getPrime(size)

        self.hashArray = [None]*size
        self.size = size
        self.removedItem = {"key": self.REMOVED_KEY}
        self.hashStep = self.hashDouble

    def getPrime(self, min):
        i = min + 1
        while True:
            if self.isPrime(i):
                return i
            i += 1

    def isPrime(self, n):
        """ Check n is prime number """
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def hash(self, key):
        return key % self.size

    def hashDouble(self, key):
        """  """
        # non-zero, less than array size, different from hash()
        # array size must be relatively prime to 5, 4, 3, and 2
        return 5 - key % 5

    def hashLinear(self, key):
        return 1

    def insert(self, data):
        """ Insert data to HashTable. Data shoud be {'key': [some int val], 'value': [any val]} """
        hashVal = self.hash(data["key"])
        stepSize = self.hashStep(data["key"])
        while self.hashArray[hashVal] != None and self.hashArray[hashVal]["key"] != self.REMOVED_KEY:
            hashVal += stepSize
            hashVal %= self.size  # wraparound array if necessary
        
        self.hashArray[hashVal] = data

    def delete(self, key):
        hashVal = self.hash(key)
        stepSize = self.hashStep(key)
        while self.hashArray[hashVal] != None and self.hashArray[hashVal]["key"] != key:
            hashVal += stepSize
            hashVal %= self.size

        val = self.hashArray[hashVal]
        self.hashArray[hashVal] = self.removedItem
        return val

    def find(self, key):
        """ Find value by key """
        hashVal = self.hash(key)
        stepSize = self.hashStep(key)
        while self.hashArray[hashVal] != None and self.hashArray[hashVal]["key"] != key:
            hashVal += stepSize
            hashVal %= self.size
        
        return self.hashArray[hashVal]

    def __str__(self):
        s = ''
        for i, item in enumerate(self.hashArray):
            s = '{}{} {}\n'.format(s, i, str(item))
        return s

if __name__ == "__main__":
    data = [1, 38, 37, 16, 20, 3, 11, 24, 5, 16, 10, 31, 18, 12, 30, 1, 19, 36, 41, 15, 25]
    ht = HashTable(23)
    for el in data:
        ht.insert({"key": el, "hash": ht.hash(el), "step": ht.hashStep(el)})
    #ht.delete(41)
    print(ht)
    #print(ht.find(25))

