from data_structures.linked_list import LinkedList
"""graph structure realisation without build-in structures"""


class Node:
    def __init__(self, data):
        self.links_list = GraphLinkedList()
        self.data = data
        self.next = None


class GraphLinkedList(LinkedList):
    """custom linked list for graph"""
    def __init__(self):
        super(GraphLinkedList, self).__init__()

    def lookup_link(self, data):
        """return link to node by data"""
        start = self.head
        while start:
            if start.data.data == data:
                return start.data
            if start.next is None:
                break
            start = start.next

    def append(self, data):
        """add element to the end"""
        new_node = Node(data)
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node

    def lookup_nodelink(self, node):
        """check if node exist"""
        start = self.head
        while start:
            if start.data == node:
                return start.data
            else:
                if start.next is not None:
                    start = start.next
                else:
                    return None

    def clear_links(self, node):
        """clear links to vertexes inside nodes"""
        start = self.head
        while start:
            start.data.links_list.delete(node)
            if start.next is None:
                break
            else:
                start = start.next

    def delete(self, node):
        """delete nodes"""
        start = self.head
        parent = self.head
        while start:
            if start.data == node:
                parent.next = start.next
                break
            else:
                if start.next is not None:
                    parent = start
                    start = start.next
                else:
                    break


class Graph:
    """Graph structure class"""
    def __init__(self):
        self.__graph = GraphLinkedList()

    def insert(self, new_node, *args):
        """insert Vertex with links to other nodes"""
        if self.__is_no_nodes(new_node, args):
            for i in args:
                new_node.links_list.append(i)
                i.links_list.append(new_node)
            self.__graph.append(new_node)
        else:
            raise ValueError

    def __is_no_nodes(self, new_node, *args):
        """check if no nodes"""
        flag = True
        if self.__graph.lookup_nodelink(new_node) is None:
            for i in args:
                if self.__graph.lookup_nodelink(i) is not None:
                    flag = False
        else:
            flag = False
        return flag

    def get_grapth(self):
        """return private modified linked list"""
        return self.__graph

    def lookup(self, data):
        """get node"""
        if self.__graph.lookup_link(data):
            return self.__graph.lookup_link(data)
        else:
            raise ValueError

    def delete(self, node):
        """delete node from graph.linkedlist"""
        self.__graph.delete(node)

    def delete_node(self, node):
        """delete vertexes from linked list inside node"""
        llist = node.links_list
        llist.clear_links(node)
        self.__graph.delete(node)
