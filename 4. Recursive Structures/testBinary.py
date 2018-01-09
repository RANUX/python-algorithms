"""
    Test cases for Binary Tree that allows duplicates

    Author: George Heineman
"""
import unittest

from my.binary import BinaryTree
import random


class TestBinaryWithDuplicates(unittest.TestCase):
    
    def setUp(self):
        self.bst = BinaryTree()
        
    def tearDown(self):
        self.bst = None
    
    def test_addValues(self):
        self.fillTree()

    def test_removeValues(self):
        self.fillTree()
        self.bst.remove(3)
        self.assertEqual(2, self.bst.root.left.value)
        self.assertEqual(None, self.bst.root.left.left.right)

    def test_closest(self):
        self.fillTree()
        self.assertEqual(7, self.bst.closest(10))
        self.assertEqual(1, self.bst.closest(-3))

    def fillTree(self):
        #      5
        #    3   7
        #   2 4    
        #  1       
        self.bst.add(5)
        self.assertEqual(5, self.bst.root.value)
        self.bst.add(3)
        self.assertEqual(3, self.bst.root.left.value)
        self.bst.add(2)
        self.assertEqual(2, self.bst.root.left.left.value)
        self.bst.add(1)
        self.assertEqual(1, self.bst.root.left.left.left.value)
        self.bst.add(4)
        self.assertEqual(4, self.bst.root.left.right.value)
        self.bst.add(7)
        self.assertEqual(7, self.bst.root.right.value)

    def test_duplicate(self):
        self.bst.add(88)
        self.bst.add(88)
        self.assertTrue(88 in self.bst)
        self.bst.remove(88)
        self.assertTrue(88 in self.bst)
        self.bst.remove(88)
        self.assertFalse(88 in self.bst)

    def test_range(self):
        match = [1,5,2,6,3,7,9,8]
        for _ in match:
            self.bst.add(_)

        self.assertEqual(1, self.bst.getMin())
        self.assertEqual(9, self.bst.getMax())

    def test_innorder(self):
        lst = [5,4,2,7,8,1]
        bt = BinaryTree()
        for _ in lst: bt.add(_)

        g = bt.root.inorder()

        for _ in sorted(lst):
            self.assertEqual(_, next(g))
        
        with self.assertRaises(StopIteration):
            next(g)

    def test_preorder(self):
        lst = [2,1,4,3,5]
        bt = BinaryTree()
        for _ in lst: bt.add(_)

        g = bt.root.preorder()

        for _ in lst:
            self.assertEqual(_, next(g))
        
        with self.assertRaises(StopIteration):
            next(g)

    def test_postorder(self):
        lst = [2,1,4,3,5]
        lstExp = [1,3,5,4,2]
        bt = BinaryTree()
        for _ in lst: bt.add(_)

        g = bt.root.postorder()

        for _ in lstExp:
            self.assertEqual(_, next(g))
        
        with self.assertRaises(StopIteration):
            next(g)

    def test_iter(self):
        match = [1,5,2,6,3,7,9,8]
        for _ in match:
            self.bst.add(_)

        compare = list(iter(self.bst))
        self.assertEqual(sorted(match), compare)
        
    def test_trial(self):
        num = 1000
        values = list(range(num))
        random.shuffle(values)
        for _ in values:
            self.bst.add(_)

        for _ in range(num):
            t = min(self.bst)
            self.bst.remove(t)
            self.assertFalse(t in self.bst)

if __name__ == '__main__':
    unittest.main()
