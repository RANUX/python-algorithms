
class HashTable(object):
    REMOVED_KEY = -1

    def __init__(self, size):
        self.hashArray = [None]*size
        self.size = size
        self.removedItem = {"key": self.REMOVED_KEY}

    def hash(self, key):
        return key % self.size

    def insert(self, data):
        """ Insert data to HashTable. Data shoud be {'key': [some int val], 'value': [any val]} """
        hashVal = self.hash(data["key"])

        while self.hashArray[hashVal] != None and self.hashArray[hashVal]["key"] != self.REMOVED_KEY:
            hashVal += 1
            hashVal %= self.size  # wraparound array if necessary
        
        self.hashArray[hashVal] = data

    def delete(self, key):
        hashVal = self.hash(key)

        while self.hashArray[hashVal] != None and self.hashArray[hashVal]["key"] != key:
            hashVal += 1
            hashVal %= self.size

        val = self.hashArray[hashVal]
        self.hashArray[hashVal] = self.removedItem
        return val

    def find(self, key):
        """ Find value by key """
        hashVal = self.hash(key)

        while self.hashArray[hashVal] != None and self.hashArray[hashVal]["key"] != key:
            hashVal += 1
            hashVal %= self.size
        
        return self.hashArray[hashVal]

    def __str__(self):
        return str(self.hashArray)

if __name__ == "__main__":
    ht = HashTable(10)
    ht.insert({"key": 20, "value": "first"})
    ht.insert({"key": 59, "value": "second"})
    ht.delete(20)
    ht.insert({"key": 69, "value": "third"})
    print(ht)
    print(ht.find(79))

