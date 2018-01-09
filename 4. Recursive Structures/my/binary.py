import sys
sys.path.append('../../../')
from utils import _build_tree_string

class BinaryNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  def add(self, val):
    if val <= self.value:
      self.left = self.addToSubTree(self.left, val)
    elif val > self.value:
      self.right = self.addToSubTree(self.right, val)

  def addToSubTree(self, parent, val):
    if parent is None:
      return BinaryNode(val)

    parent.add(val)
    return parent

  # def remove(self, val):
  #   if val < self.value:
  #     self.left = self.removeFromParent(self.left, val)
  #   elif val > self.value:
  #     self.right = self.removeFromParent(self.right, val)
  #   else:
  #     if self.left is None:   # left node has no subtree
  #       return self.right

  #     # find largest value in left subtree
  #     child = self.left
  #     while child.right:     # find largest right child
  #       child = child.right

  #     childKey = child.value
  #     self.left = self.removeFromParent(self.left, childKey)
  #     self.value = childKey
  #   return self

  # def removeFromParent(self, parent, val):
  #   if parent:
  #     return parent.remove(val)
  #   return None

  def remove(self, key, d=False):
    root = self
    current = root
    parent = root
    isLeftChild = True

    # find del node
    while current.value != key:
      parent = current
      if key < current.value:   # move left
        isLeftChild = True
        current = current.left
      else:                     # move right
        isLeftChild = False
        current = current.right

      if current == None:       # not found
        return root

    # if node is leaf or root
    if current.left == None and current.right == None:
      if current == root:
        return None
      elif isLeftChild:
        parent.left = None
      else:
        parent.right = None

    # if current deleted node only has left child
    elif current.right == None:
      if current == root:
        return current.left
      if isLeftChild:           # parent left
        parent.left = current.left
      else:                     # parent right
        parent.right = current.left
    # if current deleted node only has right child
    elif current.left == None:
      if current == root:
        return current.right
      if isLeftChild:
        parent.left = current.right
      else:
        parent.right = current.right
    else:
      #  two children, so replace with inorder successor
      #  get successor of node to delete (current)
      #  connect parent of current to successor instead
      successor = self.getSuccessorLeft(current)

      if current == root:
        #  if getSuccessorRight change right to left
        successor.right = current.right
        return successor
      elif isLeftChild:
        parent.left = successor
      else:
        parent.right = successor
      #  connect successor to current's left child
      #  if getSuccessorRight change right to left
      successor.right = current.right
    return root

  #  returns node with next-highest value after delNode
  #  goes to right child, then right child's left descendents
  def getSuccessorRight(self, delNode):
      """Find smallest successor in right subtree"""
      successorParent = delNode
      successor = delNode
      current = delNode.right
      #  go to right child
      while current != None:
          #  until no more
          #  left children,
          successorParent = successor
          successor = current
          current = current.left
          #  go to left child
      #  if successor not
      if successor != delNode.right:
          #  right child,
          #  make connections
          successorParent.left = successor.right
          successor.right = delNode.right
      return successor

  def getSuccessorLeft(self, delNode):
      """Find largest succesor in right subtree"""
      successorParent = delNode
      successor = delNode
      current = delNode.left
      #  go to right child
      while current != None:
          #  until no more
          #  left children,
          successorParent = successor
          successor = current
          current = current.right
          #  go to left child
      #  if successor not
      if successor != delNode.left:
          #  right child,
          #  make connections
          successorParent.left = successor.left
          successor.left = delNode.left
      return successor

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

  def inorder(self):
    if self.left:
      for v in self.left.inorder():
        yield v
    
    yield self.value

    if self.right:
      for v in self.right.inorder():
        yield v

  def preorder(self):
    yield self.value

    if self.left:
      for v in self.left.preorder():
        yield v

    if self.right:
      for v in self.right.preorder():
        yield v

  def postorder(self):
    if self.left:
      for v in self.left.postorder():
        yield v

    if self.right:
      for v in self.right.postorder():
        yield v
    
    yield self.value

  def printPostOrder(self):
    for v in self.postorder():
      print(v)

  def printPreOrder(self):
    for v in self.preorder():
      print(v)

  def printInOrder(self):
    for v in self.inorder():
      print(v)


class BinaryTree:
  def __init__(self, *initVals):
    self.root = None
    for _ in initVals:
      self.add(_)

  def add(self, value):
    if self.root == None:
      self.root = BinaryNode(value)
    else:
      self.root.add(value)

  def __contains__(self, target):
    n = self.root
    while n:
      if target < n.value:
        n = n.left
      elif target > n.value:
        n = n.right
      else:                  # target == n.value
        return True

    return False

  def closest(self, target):
    if self.root is None:
      return None

    n = best = self.root
    distance = abs(self.root.value - target)
    while n:
      if abs(n.value - target) < distance:
        distance = abs(n.value - target)
        best = n
      if target < n.value:
        n = n.left
      elif target > n.value:
        n = n.right
      else:
        return target

    return best.value


  def getMin(self):
    if self.root is None:
      raise ValueError("Binary Tree is empty")

    n = self.root
    while n.left:
      n = n.left
    return n.value

  def getMax(self):
    if self.root is None:
      raise ValueError("Binary Tree is empty")

    n = self.root
    while n.right:
      n = n.right
    return n.value
  
  def remove(self, value):
    if self.root is not None:
      self.root = self.root.remove(value)

  def __repr__(self):
    if self.root is None:
        return "binary:()"
    return "binary:" + str(self.root)

  def __iter__(self):
    """In order traversal of elements in the tree."""
    if self.root:
        for e in self.root.inorder():
            yield e

  def traverseDisplay(self):
    if self.root:
      self.root.traverseDisplay()



if __name__ == "__main__":
  bt = BinaryTree(4,9,6,5,7)
  print(bt.root)
  bt.remove(4)
  print(bt.root)
