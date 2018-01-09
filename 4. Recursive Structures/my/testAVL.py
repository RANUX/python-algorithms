import unittest

from avl import BinaryTree, BinaryNode
import random

class TestAVL(unittest.TestCase):
    
    def setUp(self):
        self.bst = BinaryTree()

        r = BinaryNode(5)
        rl = BinaryNode(3)

        r.right = BinaryNode(6)
        r.left = rl
        rl.left = BinaryNode(2)
        rl.right = BinaryNode(4)

        self.r = r

    def test_rotateRight(self):
      r = self.r.rotateright()
      self.assertEqual(3, r.value)
      self.assertEqual(2, r.left.value)
      self.assertEqual(5, r.right.value)
      self.assertEqual(4, r.right.left.value)

    def test_rotateLeft(self):
      r = self.r.rotateright()
      r = r.rotateleft()
      self.assertEqual(5, r.value)
      self.assertEqual(3, r.left.value)
      self.assertEqual(6, r.right.value)
      self.assertEqual(4, r.left.right.value)

if __name__ == '__main__':
    unittest.main()