from my.linkedList import LinkedList, LinkedNode

class QueueLinkedList(LinkedList):

    def __init__(self, *start):
      super().__init__(*start)
      self.tail = None

    def append(self, value):
      newNode = LinkedNode(value, None)
      if self.isEmpty():
          self.head = self.tail = newNode
      else:
          self.tail.next = newNode # Set end node to point newNode
          self.tail = newNode      # Set tail of first node point to newNode

    def pop(self):
      val = super().pop()
      if self.isEmpty():
        self.tail = None
      return val