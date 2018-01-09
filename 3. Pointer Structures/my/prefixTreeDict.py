# -*- coding=utf-8 -*-

wordkey = '\n' # любой символ кроме 'a'..'z' обозначающий конец слова

class PrefixTree(object):
  def __init__(self):
    self.head = {}
    self.count = 0

  def add(self, value):
    """Add value to prefix tree. Return True if updated"""
    d = self.head

    while len(value) > 0:
      c = value[0]

      if c not in d:  # если символа нет в дереве
        d[c] = {}     # создаем новое дерево
      
      d = d[c]
      value = value[1:] # получаем следующий символ

    if wordkey in d:
      return False

    d[wordkey] = True
    self.count += 1
    return True
  
  def remove(self, value):
    d = self.head
    while len(value) > 0:
      c = value[0]
      if c not in d:
        return False
  
      d = d[c]
      value = value[1:]

    if wordkey not in d:
      return False
    del d[wordkey]
    self.count -= 1
    return True

  def __contains__(self, value):
    """Determine if value is contained in the prefix tree."""
    d = self.head

    while len(value) > 0:
      c = value[0]
      if c not in d:
        return False
      d = d[c]        # go to next dict
      value = value[1:]

    return wordkey in d  # если есть терминальный символ, то нашли

  def __len__(self):
    return self.count