# -*- coding=utf-8 -*-
import sys
sys.path.append('../../../')
from utils import _build_tree_string

class BinaryNode:

  def __init__(self, value = None):
      """Create binary node."""
      self._value  = value
      self.left   = None
      self.right  = None
      self.height = 1

  @property
  def value(self):
    return '{}:{}'.format(self._value, self.height)

  def bfactor(self):
    '''Calculate balance factor'''
    return self.heightRight - self.heightLeft

  def fixHeight(self):
    hl = self.heightLeft
    hr = self.heightRight
    self.height = (hl if hl>hr else hr)+1

  @property
  def heightLeft(self):
    return self.left.height if self.left else 0

  @property
  def heightRight(self):
    return self.right.height if self.right else 0
  
  def rotateright(self):
    newParentL = self.left
    self.left = newParentL.right
    newParentL.right = self

    self.fixHeight()
    newParentL.fixHeight()

    return newParentL

  def rotateleft(self):
    newParentR = self.right
    self.right = newParentR.left
    newParentR.left = self

    self.fixHeight()
    newParentR.fixHeight()

    return newParentR

  def balance(self):
    self.fixHeight()

    if self.bfactor() == 2:
      # if self.right.left.height > self.right.right.height
      if self.right.bfactor() < 0:
        self.right = self.right.rotateright()
      return self.rotateleft()

    elif self.bfactor() == -2:
      # if self.left.right.height > self.left.left.height
      if self.left.bfactor() > 0:
        self.left = self.left.rotateleft()
      return self.rotateright()

    return self   # not need for balance

  def add(self, val):
    if val < self._value:
      if self.left == None:
        self.left = BinaryNode(val)
        return self.balance()

      self.left = self.left.add(val)
    else:
      if self.right == None:
        self.right = BinaryNode(val)
        return self.balance()

      self.right = self.right.add(val)

    return self.balance()
  
  def findMin(self, val):
    """Find node with min value"""
    return self.left.findMin(val) if self.left else self
  
  def removeMin(self):
    if self.left == None:
      return self.right

    self.left = self.left.removeMin()
    return self.balance()

  def remove(self, val):
    if val < self._value:
      if self.left == None: return None
      self.left = self.left.remove(val)

    elif val > self._value:
      if self.right == None: return None
      self.right = self.right.remove(val)
    else:                                   # if val == self.value
      left  = self.left
      right = self.right

      if right == None: return left
      min = right.findMin(val)
      min.left  = left
      min.right = right.removeMin()
      return min.balance()

    return self.balance()

  def __str__(self):
    """Return the pretty-print string for the binary tree.
    :return: The pretty-print string.
    :rtype: str | unicode
    **Example**:
    .. doctest::
        >>> from binarytree import Node
        >>>
        >>> root = Node(1)
        >>> root.left = Node(2)
        >>> root.right = Node(3)
        >>> root.left.right = Node(4)
        >>>
        >>> print(root)
        <BLANKLINE>
          __1
          /   \\
        2     3
          \\
          4
        <BLANKLINE>
    .. note::
        To include `level-order (breath-first)`_ indexes in the string, use
        :func:`binarytree.Node.pprint` instead.
    .. _level-order (breath-first):
        https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
    """
    lines = _build_tree_string(self, 0, False, '-')[0]
    return '\n' + '\n'.join((line.rstrip() for line in lines))


class BinaryTree:

  def __init__(self, *initVals):
    """Create empty binary tree."""
    self.root = None
    for _ in initVals:
      self.add(_)

  def add(self, value):
    """Insert value into proper location in Tree."""
    if self.root is None:
        self.root = BinaryNode(value)
    else:
        self.root = self.root.add(value)

  def remove(self, value):
    """Remove value from Tree."""
    if self.root is None:
        return None
    else:
        self.root = self.root.remove(value)

  def dumpTree(self):
    print(self.root)

if __name__ == "__main__":
  bt = BinaryTree(*list(range(1,20)))
  bt.dumpTree()
  bt.remove(16)
  bt.dumpTree()