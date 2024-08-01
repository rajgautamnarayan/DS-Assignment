# 1. Implement a Self Balancing Binary Search Tree with following supported operation :    (3 Marks)
# find(key) : returns true if key is present else false 
# insert(key) : insert a new key
# remove(key) : remove an existing key
# order_of_key(key) : returns the order of the key compared to the existing elements i.e., how many elements are smaller than key 
# get_by_order(k) : returns the  k’th element among the existing keys



class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def find(self, root, key):
        if not root:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self.find(root.left, key)
        else:
            return self.find(root.right, key)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def order_of_key(self, root, key):
        if not root:
            return 0
        if key < root.key:
            return self.order_of_key(root.left, key)
        elif key > root.key:
            return 1 + self.size(root.left) + self.order_of_key(root.right, key)
        else:
            return self.size(root.left)

    def size(self, node):
        if not node:
            return 0
        return self.size(node.left) + self.size(node.right) + 1

    def get_by_order(self, root, k):
        if not root:
            return None
        left_size = self.size(root.left)
        if k < left_size:
            return self.get_by_order(root.left, k)
        elif k > left_size:
            return self.get_by_order(root.right, k - left_size - 1)
        else:
            return root.key


tree = AVLTree()
root = None
keys = [20, 15, 25, 10, 18, 5, 30]

for key in keys:
    root = tree.insert(root, key)

print(tree.find(root, 15))  
print(tree.find(root, 50))  
root = tree.delete(root, 20)
print(tree.order_of_key(root, 18))  
print(tree.get_by_order(root, 3))  
