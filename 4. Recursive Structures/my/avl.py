# -*- coding=utf-8 -*-
from utils import _build_tree_string

class BinaryNode:

  def __init__(self, value = None):
      """Create binary node."""
      self.value  = value
      self.left   = None
      self.right  = None
      self.height = 1

  def bfactor(self):
    '''Calculate balance factor'''
    return self.heightRight - self.heightLeft

  def fixheight(self):
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
    newRootL = self.left
    self.left = newRootL.right
    newRootL.right = self

    self.fixheight()
    newRootL.fixheight()

    return newRootL

  def rotateleft(self):
    newRootR = self.right
    self.right = newRootR.left
    newRootR.left = self

    self.fixheight()
    newRootR.fixheight()

    return newRootR

  def balance(self):
    self.fixheight()

    if self.bfactor() == 2:
      if self.right.bfactor() < 0:
        self.right = self.right.rotateright()
      return self.rotateleft()

    elif self.bfactor() == -2:
      if self.left.bfactor() > 0:
        self.left = self.left.rotateleft()
      return self.rotateright()

    return self   # not need for balance

  def add(self, val):
    if val < self.value:
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
    """Insert value into proper location in Binary Tree."""
    if self.root is None:
        self.root = BinaryNode(value)
    else:
        self.root = self.root.add(value)

  def dumpTree(self):
    print(self.root)

if __name__ == "__main__":
  bt = BinaryTree(*list(range(0,21)))
  bt.dumpTree()