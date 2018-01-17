import unittest
from tree234 import Tree234

class Test234(unittest.TestCase):
    
    def setUp(self):
        self.tree = Tree234()
        self.data = [30, 50, 70, 40, 20, 80, 25, 90, 75, 10]
    
    def test_insert(self):
        for v in self.data:
            self.tree.insert(v)

        self.assertEqual(list(self.tree), sorted(self.data))

if __name__ == '__main__':
    unittest.main()