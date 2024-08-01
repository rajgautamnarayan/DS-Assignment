# 2.Implement a Hashmap with following supported operation : (3 Marks)
# find(key) : returns true if key is present else false
# insert(key, value) : insert a new {key, value} pair
# remove(key) : remove an existing key
# Implement both open addressing (Linear and/or Quadratic probing) and separate chaining techniques for collision handling



# Separate Chaining Implementation

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def find(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return

    def __str__(self):
        return str(self.table)


hashmap = HashMapSeparateChaining()
hashmap.insert('a', 1)
hashmap.insert('b', 2)
print(hashmap.find('a'))  
print(hashmap.find('c'))  
hashmap.remove('a')
print(hashmap.find('a'))  




#Open Addressing Implementation


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def find(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return True
            index = (index + 1) % self.size
        return False

    def remove(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size


hashmap = HashMapOpenAddressing()
hashmap.insert('a', 1)
hashmap.insert('b', 2)
print(hashmap.find('a'))  
print(hashmap.find('c'))  
hashmap.remove('a')
print(hashmap.find('a')) 



