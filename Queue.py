# This algorithm follows First Come First Out(FIFO)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqeue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
            self.length -= 1




    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_queue = MyQueue(4)
my_queue.enqeue(2)
my_queue.enqeue(5)
my_queue.dequeue()

my_queue.print_queue()
