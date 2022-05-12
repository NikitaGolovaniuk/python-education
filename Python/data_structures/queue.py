from data_structures.linked_list import LinkedList
"""Queue structure realisation"""


class Queue(LinkedList):
    """Queue structure based on LinkedList"""
    def __init__(self):
        super(Queue, self).__init__()

    def enqueue(self, data):
        """add to queue"""
        self.append(data)

    def dequeue(self):
        """get element"""
        start = self.head
        while start.next:
            start = start.next
        index = self.lookup(start.data)
        tmp = start.data
        self.delete(index)
        return tmp

    def peek(self):
        """get first element"""
        start = self.head
        while start.next:
            start = start.next
        return start.data
