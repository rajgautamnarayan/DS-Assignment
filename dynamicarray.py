class DynamicArray:
    def __init__(self, initial_capacity=10, resize_factor=1.5):
        self.array = [0] * initial_capacity
        self.capacity = initial_capacity
        self.size = 0
        self.resize_factor = resize_factor

    def resize(self):
        new_capacity = int(self.capacity * self.resize_factor)
        new_array = [0] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert_at(self, index, value):
        if index > self.size:
            print("Index out of range")
            return
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def delete_at(self, index):
        if index >= self.size:
            print("Index out of range")
            return
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate_right(self, k):
        if self.size == 0:
            return
        k %= self.size
        temp = self.array[-k:] + self.array[:-k]
        self.array[:self.size] = temp

    def reverse(self):
        self.array[:self.size] = self.array[:self.size][::-1]

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = value
        self.size += 1

    def prepend(self, value):
        self.insert_at(0, value)

    @staticmethod
    def merge(a, b):
        result = DynamicArray(a.size + b.size)
        for i in range(a.size):
            result.append(a.array[i])
        for i in range(b.size):
            result.append(b.array[i])
        return result

    @staticmethod
    def interleave(a, b):
        new_size = a.size + b.size
        result = DynamicArray(new_size)
        min_size = min(a.size, b.size)
        for i in range(min_size):
            result.append(a.array[i])
            result.append(b.array[i])
        for i in range(min_size, a.size):
            result.append(a.array[i])
        for i in range(min_size, b.size):
            result.append(b.array[i])
        return result

    def middle_element(self):
        if self.size == 0:
            print("Array is empty")
            return -1
        return self.array[self.size // 2]

    def index_of(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def split_at(self, index):
        if index > self.size:
            print("Index out of range")
            return None, None
        first = DynamicArray(index)
        second = DynamicArray(self.size - index)
        for i in range(index):
            first.append(self.array[i])
        for i in range(index, self.size):
            second.append(self.array[i])
        return first, second

    def set_resize_factor(self, factor):
        if factor <= 1.0:
            print("Resize factor must be greater than 1.0")
            return
        self.resize_factor = factor


# Testing the DynamicArray class
if __name__ == "_main_" :
    arr = DynamicArray()

    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.prepend(0)

    print("Array after appending and prepending: ", end="")
    for i in range(arr.get_size()):
        print(arr.middle_element(), end=" ")
    print()

    arr.insert_at(2, 10)
    print("Array after inserting 10 at index 2: ", end="")
    for i in range(arr.get_size()):
        print(arr.middle_element(), end=" ")
    print()

    arr.delete_at(2)
    print("Array after deleting element at index 2: ", end="")
    for i in range(arr.get_size()):
        print(arr.middle_element(), end=" ")
    print()

    arr.rotate_right(2)
    print("Array after rotating right by 2: ", end="")
    for i in range(arr.get_size()):
        print(arr.middle_element(), end=" ")
    print()

    arr.reverse()
    print("Array after reversing: ", end="")
    for i in range(arr.get_size()):
        print(arr.middle_element(), end=" ")
    print()