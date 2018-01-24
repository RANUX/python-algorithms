

class LinkNode:
    def __init__(self, key, tail = None):
        """Node in a Linked List."""
        self.key = key
        self.next  = tail

    def __str__(self):
        return 'key: {}'.format(self.key)

class SortedLinkedList:
    def __init__(self, *start):
        """Demonstrate linked lists in Python."""
        self.head  = None
        for _ in start:
            self.insert(_)

    def insert(self, key):
        node = LinkNode(key)
        key = node.key
        previous = None
        current = self.head

        while current != None and current.key < key:
            previous = current
            current = current.next
        
        if previous == None:
            self.head = node
        else:
            previous.next = node

        node.next = current

    def remove(self, key):
        previous = None
        current = self.head

        while current != None and current.key != key:
            previous = current
            current = current.next

        if previous == None:                # if beginning of list
            self.head = self.head.next      # delete first link
        else:
            previous.next = current.next    # delete current link
    
    def find(self, key):
        current = self.head
        while current != None and current.key <= key:
            if current.key == key:
                return current
            current = current.next

        return None

    def __repr__(self):
        """String representation of linked list."""
        if self.head is None:
            return 'link:[]'

        return 'link:[{0:s}]'.format(','.join(map(str,self)))

    def __len__(self):
        """Count values in list."""
        n = self.head
        count = 0
        while n != None:
          count += 1
          n = n.next
        return count

    def __iter__(self):
        """Iterator of values in the list."""
        n = self.head
        while n != None:
            yield n.key
            n = n.next