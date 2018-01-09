"""
    Demonstration of Linked Lists in Python.

    Author: George Heineman
"""
class LinkedNode:
    def __init__(self, value, tail = None):
        """Node in a Linked List."""
        self.value = value
        self.next  = tail

    def checkInfinite(self):
        p1 = p2 = self
        while p1 != None and p2 != None:
            if p2.next == None: return False
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2: return True
        return False


class LinkedList:
    def __init__(self, *start):
        """Demonstrate linked lists in Python."""
        self.head  = None
        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        """Prepend element into list."""
        self.head = LinkedNode(value, self.head)

    def pop(self):
        """Remove first value in list."""
        if not self.head:
          raise Exception ("Linked list is empty.")

        value = self.head.value
        self.head = self.head.next
        return value

    def remove(self, value):
        """Remove value from list."""
        n = self.head
        prev = None
        while n != None:
          if n.value == value:
            if prev:
              prev = n.next
            else:
              self.head = n.next
            return True

          n = n.next
          prev = n
        return False

    def contains(self, value):
        n = self.head
        while n != None:
            if n.value == value:
                return True
            n = n.next

    def __iter__(self):
        """Iterator of values in the list."""
        n = self.head
        while n != None:
          yield n.value
          n = n.next
        
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

    def isEmpty(self):
      return self.head is None