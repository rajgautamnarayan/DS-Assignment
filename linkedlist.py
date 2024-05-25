class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def _init_(self):
        self.head = None
        self.listSize = 0

    def _del_(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node

    def insert_at(self, index, value):
        if index > self.listSize:
            print("Index out of range")
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = None
            curr = self.head
            for i in range(index):
                prev = curr
                curr = curr.next
            new_node.next = curr
            prev.next = new_node
        self.listSize += 1

    def delete_at(self, index):
        if index >= self.listSize:
            print("Index out of range")
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
        else:
            prev = None
            for i in range(index):
                prev = temp
                temp = temp.next
            prev.next = temp.next
        del temp
        self.listSize -= 1

    def get_size(self):
        return self.listSize

    def is_empty(self):
        return self.listSize == 0

    def rotate_right(self, k):
        if self.listSize == 0:
            return
        k = k % self.listSize
        if k == 0:
            return

        old_tail = self.head
        new_tail = self.head
        new_head = self.head

        for i in range(self.listSize - 1):
            old_tail = old_tail.next
        for i in range(self.listSize - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        old_tail.next = self.head
        new_tail.next = None
        self.head = new_head

    def reverse(self):
        prev = None
        curr = self.head
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.listSize += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.listSize += 1

    @staticmethod
    def merge(a, b):
        result = SinglyLinkedList()
        temp = a.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        temp = b.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    @staticmethod
    def interleave(a, b):
        result = SinglyLinkedList()
        temp_a = a.head
        temp_b = b.head
        while temp_a or temp_b:
            if temp_a:
                result.append(temp_a.data)
                temp_a = temp_a.next
            if temp_b:
                result.append(temp_b.data)
                temp_b = temp_b.next
        return result

    def middle_element(self):
        if self.listSize == 0:
            print("List is empty")
            return -1
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def index_of(self, value):
        temp = self.head
        for i in range(self.listSize):
            if temp.data == value:
                return i
            temp = temp.next
        return -1

    def split_at(self, index):
        if index > self.listSize:
            print("Index out of range")
            return None, None
        first = SinglyLinkedList()
        second = SinglyLinkedList()
        temp = self.head
        for i in range(index):
            first.append(temp.data)
            temp = temp.next
        while temp:
            second.append(temp.data)
            temp = temp.next
        return first, second

    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("null")

# Testing the SinglyLinkedList class
if __name__ == "_main_":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.prepend(0)
    sll.print_list()

    sll.insert_at(2, 10)
    print("After inserting 10 at index 2: ", end="")
    sll.print_list()

    sll.delete_at(2)
    print("After deleting element at index 2: ", end="")
    sll.print_list()

    sll.rotate_right(2)
    print("After rotating right by 2: ", end="")
    sll.print_list()

    sll.reverse()
    print("After reversing: ", end="")
    sll.print_list()

    list1 = SinglyLinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = SinglyLinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    merged_list = SinglyLinkedList.merge(list1, list2)
    print("Merged list: ", end="")
    merged_list.print_list()

    interleaved_list = SinglyLinkedList.interleave(list1, list2)
    print("Interleaved list: ", end="")
    interleaved_list.print_list()

    print(f"Middle element of the list: {sll.middle_element()}")

    print(f"Index of element 3: {sll.index_of(3)}")

    first_half, second_half = sll.split_at(2)
    print("First half: ", end="")
    first_half.print_list()
    print("Second half: ", end="")