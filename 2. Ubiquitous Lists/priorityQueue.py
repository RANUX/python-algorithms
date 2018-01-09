
class PriorityQueue:
  
  def __init__(self):
    self.clear()

  def __len__(self):
        """Return number of elements"""
        return len(self.queue)

  def clear(self):
    self.queue = []
    self.count = 0

  def enqueue(self, value, compare=lambda a,b: a > b):
    pos = 0
    for j in range(self.count-1, -1, -1):
      if compare(value, self.queue[j]):   # if new value larger
        if j+1 < self.count:
          self.queue[j+1] = self.queue[j]   # shift upward
        else:
          self.queue.insert(j+1, self.queue[j])
      else:
        pos = j+1
        break
    
    if pos < self.count:
      self.queue[pos] = value
    else:
      self.queue.insert(pos, value)

    self.count += 1


  def dequeue(self):
    self.count -= 1
    return self.queue[self.count];

  def size(self):
    return self.count
  
  def isEmpty(self):
    """Determines if queue is empty."""
    return self.count == 0

  def peekFront(self):
    return self.queue[self.count-1]

  def peekRear(self):
    if self.isEmpty():
        raise RangeError('PriorityQueue is Empty.')
    return self.queue[0];
