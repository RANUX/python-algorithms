import unittest
import sys
sys.path.append('../../')
from priorityQueue import PriorityQueue
from utils import knuth_shuffle

class TestPriorityQueue(unittest.TestCase):
    
    def setUp(self):
        self.pq = PriorityQueue()

    def tearDown(self):
        self.pq = None

    def test_basic(self):
      self.assertTrue(self.pq.isEmpty())
      self.assertEqual(0, len(self.pq))

    def test_fill(self):
      """Fill up the queue."""
      data = knuth_shuffle(range(1,10))
      for d in data:
        self.pq.enqueue(d)
      
      sorted_data = sorted(data)
      self.assertEqual(sorted_data[0], self.pq.peekFront())
      self.assertEqual(sorted_data[len(sorted_data)-1], self.pq.peekRear())
      self.assertEqual(len(data), len(self.pq))

      for d in sorted_data:
        self.assertEqual(d, self.pq.dequeue())

      self.assertTrue(self.pq.isEmpty())


if __name__ == '__main__':
    unittest.main()