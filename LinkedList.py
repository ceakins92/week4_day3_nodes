from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            previous_node = current_node
            while current_node.right:
                current_node = current_node.right
                current_node.left = previous_node
            current_node.right = node

    def __iter__(self):  # Allows looping through the lists and methods
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.value)
        return ' -> '.join(nodes)

    def insert_node(self, target, value):
        new_node = Node(value)
        if self.head:
            for node in self:
                if node.value == target:
                    right_node = node.right
                    node.right = new_node
                    new_node.right = right_node
        else:
            print('Empty List')

    def remove_node(self, value):
        if value == self.head.value:
            self.head = self.head.right
        else:
            for node in self:
                if node.right.value == value:
                    node.right = node.right.right
                    return

    def insert_prior(self, target, value):
        new_node = Node(value)
        if self.head:
            if self.head.value == target:
                right_node = self.head
                self.head = new_node
                new_node.right = right_node
            for node in self:
                if node.right.value == target:
                    right_node = node.right
                    node.right = new_node
                    new_node.right = right_node
                    return
        else:
            print("empty list")

    def get_tail(self):
        # for node in self:
        # pass
        # return node.value
        node = self.head
        while node.right:
            node = node.right
        return node.value

    def remove_tail(self):
        node = self.head
        if node.right:
            while node.right.right:
                node = node.right
        node.right = None

# Start by creating a new method in our LinkedList class called "add_list_elements".
# This method should take in a list as an argument.
# Loop through each element in the list and convert it to a node.
# Add each node to the end of the linked list using the "add_node" method we already have in the class.

    def take_list(self, alist):
        for addme in alist:
            self.add_node(addme)

# linked_list.take_list(['Oneday', 'Someday', 'Anotherday', 'Anyday'])
# print(linked_list)


linked_list = LinkedList()
linked_list.add_node('Sunday')
linked_list.add_node('Monday')
linked_list.add_node('Tuesday')
linked_list.add_node('Thursday')
print(linked_list.head.right.value)


print(linked_list)

linked_list.insert_node('Tuesday', 'Wednesday')
print(linked_list)
linked_list.add_node('Spazday')
print(linked_list)
linked_list.remove_node('Sunday')
print(linked_list)
linked_list.remove_node('Spazday')
print(linked_list)
linked_list.insert_prior('Tuesday', 'Testday')
print(linked_list)
linked_list.take_list(['Oneday', 'Someday', 'Anotherday', 'Anyday'])
print(linked_list)
