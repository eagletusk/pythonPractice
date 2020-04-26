class Deque(object):
  def __init__(self):
    self.items = []

  def addFront(self,item):
    self.items.append(item)

  def addRear(self, item):
    self.items.insert(len(self.items),item)

  def removeFront(self):
    return self.items.pop(0)

  def removeBack(self):
    return self.items.pop()

  def isEmpty(self):
    return self.items == []

  def size(self):
    return len(self.items)

k = Deque()
k.addFront(3)
k.addFront(4)
k.addRear(1)
k.addRear(2)
print(k.items)
k.removeFront()
print(k.items)
k.removeBack()
print (k.items)
print(k.isEmpty())
print(k.size())