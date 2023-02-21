import math

class HashTable:
  def __init__(self, number_of_buckets):
    self.number_of_buckets = number_of_buckets
    self.table = [ [] for i in range(number_of_buckets)]
    pass

  def hash(self, key):
    num = 0
    for char in key:
      num += ord(char)
    m = 0.5*(math.sqrt(5)-1)
    m = m + num
    hashed = math.floor(m % self.number_of_buckets)
    return hashed

  def set_value(self, key, value):
    # here is where you'll perform your logic to insert the value into your table
    # you'll also call your hash method here to get the index where you'll store the value
    index = self.hash(key)
    print(index)
    self.table[index].append[(key, value)]


  def get_value_by_key(self, key):
    # here is where you'll retreive your value from the hash table
    # IMPORTANT: Think about how you'd retreive a value that from an index that has multiple values
    index = self.hash(key)
    for data in self.table[index]:
      print(data)

  def has_key(self, value):
    # here is where you'll return a True or False value if there is a value stored at a specific index in your HashTable
    pass


my_table = HashTable(64)
my_table.set_value('name', 'alice')
print(my_table.get_value_by_key("name"))