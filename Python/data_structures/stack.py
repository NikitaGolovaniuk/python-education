from data_structures.linked_list import LinkedList
"""Stack structure"""


class Stack(LinkedList):
    """Stack structure inherited from LinkedList"""
    def __init__(self):
        super(Stack, self).__init__()

    def push(self, data):
        """add element to stack"""
        self.prepend(data)

    def pop(self):
        """remove element from stack"""
        self.delete(0)

    def peek(self):
        """get peek"""
        return self.head.data
