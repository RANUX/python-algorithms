from linkedList import LinkedList

def sum(n):
  if n == None:
    return 0

  return n.value + sum(n.next)

if __name__ == "__main__":
  l = LinkedList(3, 5, 2, 6)
  print(sum(l.head))