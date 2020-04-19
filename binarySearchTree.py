def go():
  class Node:
    def __init__(self, val):
      self.value = val
      self.leftChild = None
      self.rightChild = None

    def insert(self, data):
      if self.value == data:
        return False
      elif self.value > data: 
        if self.leftChild:
          return self.leftChild.insert(data)
        else:
          self.leftChild = Node(data)
          return True
      else:
        if self.rightChild:
          return self.rightChild.insert(data)
        else: 
          self.rightChild = Node(data)
          return True

    def find(self,data):
      if(self.value == data):
        return True
      elif self.value > data:
        if self.leftChild:
          return self.leftChild.find(data)
        else:
          return False
      else:
        if self.rightChild:
          return self.rightChild.find(data)
        else:
          return False

    def preorder(self):
      if self:
        print(str(self.value))
        if self.leftChild:
          self.leftChild.preorder()
        if self.rightChild:
          self.rightChild.preorder()

      
  class Tree:
    def __init__(self):
      self.root = None

    def insert (self,data):
      if self.root:
        return self.root.insert(data)
      else:
        self.root = Node(data)
        return True

    def find(self,data):
      if self.root: 
        return self.root.find(data)
      else: 
        return False

    def preorder(self):
      print("preorder")
      self.root.preorder()

  bst = Tree()
  print(bst.insert(10))
  bst.insert(0)
  bst.insert(2)
  bst.insert(45)
  bst.insert(1)
  bst.insert(22)
  bst.insert(452)
  bst.preorder()
  print('done')
