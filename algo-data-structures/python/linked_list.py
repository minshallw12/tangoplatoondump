# ----- Node ------
class Node:
  def __init__(self, value):
    self.value = value
    self.nextNode = None


class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node 
  # in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self):
    self.head = None
    self.length = 0

  def add(self, data):
    if self.head == None:
      self.head = Node(data)
    else:
      currentNode = self.head
      while currentNode.nextNode != None:
        currentNode = currentNode.nextNode
      currentNode.nextNode = Node(data)
      self.length += 1

    # write your code to ADD an element to the Linked List
    # self.length += 1
    # if self.head == None:
    #   self.head = Node(data)
    #   return
    # current = self.head
    # while current.nextNode!= None:
    #   current = current.nextNode
    # current.nextNode = Node(data)
    # current.nextNode.nextNode = None
      

  def remove(self, data):
    if self.head == None:
      return
    if self.head.value == data:
      self.head = self.head.nextNode
      return
    current = self.head
    while current.nextNode != None:
      if current.nextNode.value == data:
        current.nextNode = current.nextNode.nextNode
        return
      current = current.nextNode
      break   

  def get(self, element_to_get):
    currentNode = self.head
    while currentNode.nextNode != None:
      if element_to_get == currentNode.nextNode.value:
        return currentNode.nextNode.value
      currentNode = currentNode.nextNode
        




my_list = LinkList()
my_list.add('will')
my_list.add("oranges")
my_list.add("toby")
my_list.add("kfanifg")
my_list.add(["Tiger Shark"])

print(my_list.get("oranges"))