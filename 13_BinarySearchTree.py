class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """def __init__(self, value):
        new_node = Node(value)
        self.root = new_node"""

    def __init__(self):  # We can the above constructor or as an alternative, we can  use this where jut create a
        self.root = None  # tree with no value and then add the value with insert method

    # Concept for inserting a node.
    """
    create new_node
    if root == None then root = new_node
    temp = self.root
    while loop
        if new_node == temp return False
        if < left else> right
        if None insert new_node else move to next
    """

    def insert_value(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # Concept for checking the value is present or not
    """
        if root == None return False     # This line can be ignored as there it checked in the next line
        temp = root
        while temp is not None
            if < left
            elif > right
            else = return True
        return False    
        """

    def contain_value(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BinarySearchTree()
my_tree.insert_value(2)
my_tree.insert_value(1)
my_tree.insert_value(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contain_value(3))
print(my_tree.contain_value(30))
