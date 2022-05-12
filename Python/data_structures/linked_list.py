"""Linked List realisation without build-in structures"""


class Node:
    """list element"""
    def __init__(self, data=None, next_el=None, prev_el=None):
        self.data = data
        self.next = next_el
        self.prev = prev_el


class LinkedList:
    """core class"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """add element to end"""
        new_node = Node(data)
        if self.head:
            current_node = self.head
            while current_node:
                if current_node.next is None:
                    current_node.next = new_node
                    new_node.prev = current_node
                    break
                current_node = current_node.next
        else:
            self.head = new_node

    def prepend(self, data):
        """add element to start"""
        new_node = Node(data)
        if self.head:
            current_node = self.head
            self.head = new_node
            self.head.next = current_node
            current_node.prev = new_node
        else:
            self.head = new_node

    def lookup(self, data):
        """get element index by data"""
        start = self.head
        index = 0
        while start:
            if start.data == data:
                return index
            index += 1
            if start.next is None:
                break
            start = start.next

    def insert(self, data, index):
        """insert element to position"""
        new_node = Node(data)
        if self.head:
            start = self.head
            curr_index = 0
            print(start)
            while start:
                if curr_index == index:
                    parent = start.prev
                    if parent:
                        parent.next = new_node
                        new_node.next = start
                    else:
                        self.head = new_node
                    break
                curr_index += 1
                start = start.next
        else:
            self.head = new_node

    def delete(self, index):
        """delete node"""
        start = self.head
        curr_index = 0
        while start:
            if curr_index == index and index != 0:
                parent = start.prev
                son = start.next
                parent.next = son
                break
            if index == 0:
                self.head = start.next
                break
            curr_index += 1
            start = start.next
