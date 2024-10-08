class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.tail
    #     self.tail = self.tail.prev
    #     self.tail.next = None
    #     temp.prev = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None
    #     return temp

    def pop(self):  # Alternative option
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):  # same cam be used as used for singly linked list.
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length - 1:
            return self.pop()
        before = self.get(index - 1)
        temp = before.next
        after = temp.next
        before.next = temp.next
        after.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


D_linked_list = DoubleLinkedlist(0)
# print(my_linked_list.head.value)
D_linked_list.append(2)
D_linked_list.insert(1, 1)
D_linked_list.print()
# my_linked_list.remove(1)
