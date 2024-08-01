# LeetCode Problem 225

class MyStack:

    def __init__(self):
       
        self.data = []

    def push(self, x):
        
        self.data.append(x)

    def pop(self):
        
        return self.data.pop()

    def top(self):
        
        return self.data[-1]

    def empty(self):
        
        return not bool(self.data)


# LeetCode Problem 232

class MyQueue:

    def __init__(self):
        
        self.data = []

    def push(self, x):
        
        self.data.append(x)

    def pop(self):
       
        front = self.data[0]
        self.data = self.data[1:]
        return front

    def peek(self):
        
        return self.data[0]

    def empty(self):
        
        return not bool(self.data)


# LeetCode Problem - 380

class RandomizedSet:

    def __init__(self):
        
        self.nums, self.ind = [], {}
    def insert(self, val):
        
        if val not in self.ind: 
            self.nums += val, 
            self.ind[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        
        if val in self.ind:
            ind, last = self.ind[val], self.nums[-1]
            self.nums[ind], self.ind[last] = last, ind
            self.nums.pop()
            self.ind.pop(val)
            return True
        return False

    def getRandom(self):
        
        return random.choice(self.nums)



# LeetCode Problem 381
class RandomizedCollection:

    def __init__(self):
        self.arr, self.pos = [], collections.defaultdict(set)
    def insert(self, val):
        out = val not in self.pos
        self.arr.append(val)
        self.pos[val].add(len(self.arr) - 1)
        return out

    def remove(self, val):
        if val in self.pos:
            if self.arr[-1] != val:
                x, y = self.pos[val].pop(), self.arr[-1]
                self.pos[y].discard(len(self.arr) - 1)
                self.pos[y].add(x)
                self.arr[x] = y
            else:
                self.pos[val].discard(len(self.arr) - 1)
            self.arr.pop()
            if not self.pos[val]:
                self.pos.pop(val)
            return True 
        return False

    def getRandom(self):
        return random.choice(self.arr)
    

# LeetCode Problem 707
class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
class MyLinkedList:

    def __init__(self):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
        
    def add(self, preNode, val):
        node = Node(val)
        node.pre = preNode
        node.next = preNode.next
        node.pre.next = node.next.pre = node
        self.size += 1
        
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1
        
    def forward(self, start, end, cur):
        while start != end:
            start += 1
            cur = cur.next
        return cur
    
    def backward(self, start, end, cur):
        while start != end:
            start -= 1
            cur = cur.pre
        return cur
    
    def get(self, index):
        if 0 <= index <= self.size // 2:
            return self.forward(0, index, self.head.next).val
        elif self.size // 2 < index < self.size:
            return self.backward(self.size - 1, index, self.tail.pre).val
        return -1

    def addAtHead(self, val):
        self.add(self.head, val)

    def addAtTail(self, val):
        self.add(self.tail.pre, val)

    def addAtIndex(self, index, val):
        if 0 <= index <= self.size // 2:
            self.add(self.forward(0, index, self.head.next).pre, val)
        elif self.size // 2 < index <= self.size:
            self.add(self.backward(self.size, index, self.tail).pre, val)

    def deleteAtIndex(self, index):
        if 0 <= index <= self.size // 2:
            self.remove(self.forward(0, index, self.head.next))
        elif self.size // 2 < index < self.size:
            self.remove(self.backward(self.size - 1, index, self.tail.pre))



# LeetCode Problem 901

class StockSpanner:

    def __init__(self):
        self.arr = []  
        self.res = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if self.arr and self.arr[-1] > price: self.res.append(1)
        else:
            i = len(self.arr) - 1
            while i >= 0:
                if self.arr[i] <= price and self.res[i]:
                    i -= self.res[i]
                else: break
            self.res.append(len(self.arr) - i)
        self.arr.append(price)
        return self.res[-1]
        



# Leet Code Problem 1381
class CustomStack:
  def __init__(self, maxSize: int):
    self.maxSize = maxSize
    self.stack = []
    
    self.pendingIncrements = []

  def push(self, x: int) -> None:
    if len(self.stack) == self.maxSize:
      return
    self.stack.append(x)
    self.pendingIncrements.append(0)

  def pop(self) -> int:
    if not self.stack:
      return -1
    if len(self.stack) > 1:
      self.pendingIncrements[-2] += self.pendingIncrements[-1]
    return self.stack.pop() + self.pendingIncrements.pop()

  def increment(self, k: int, val: int) -> None:
    if not self.stack:
      return
    i = min(k - 1, len(self.stack) - 1)
    self.pendingIncrements[i] += val


#LeetCode Problem 1472
class BrowserHistory:
  def __init__(self, homepage: str):
    self.urls = []
    self.index = -1
    self.lastIndex = -1
    self.visit(homepage)

  def visit(self, url: str) -> None:
    self.index += 1
    if self.index < len(self.urls):
      self.urls[self.index] = url
    else:
      self.urls.append(url)
    self.lastIndex = self.index

  def back(self, steps: int) -> str:
    self.index = max(0, self.index - steps)
    return self.urls[self.index]

  def forward(self, steps: int) -> str:
    self.index = min(self.lastIndex, self.index + steps)
    return self.urls[self.index]