"""binary tree realisation without build-in structures"""


class Node:
    def __init__(self, data):
        self.data = data
        self.less = None
        self.more = None
        self.parent = None


class BinaryTree:
    """binary tree class"""
    def __init__(self):
        self.root = None

    def insert(self, item):
        """insert element"""
        if self.root is not None:
            current = self.root
            while True:
                if current.data > item:
                    if current.less is None:
                        current.less = Node(item)
                        current.less.parent = current
                        break
                    else:
                        current = current.less
                elif current.data < item:
                    if current.more is None:
                        current.more = Node(item)
                        current.more.parent = current
                        break
                    else:
                        current = current.more
                else:
                    break
        else:
            self.root = Node(item)

    def lookup(self, data):
        """get element"""
        current = self.root
        if current:
            while True:
                if current.data > data:
                    current = current.less
                elif current.data < data:
                    current = current.more
                elif current.data == data:
                    return current
                else:
                    break
        else:
            return None

    def preorder_traversal(self, node):
        """method for printing values"""
        if node is not None:
            print(node.data)
            self.preorder_traversal(node.less)
            self.preorder_traversal(node.more)

    def delete(self, data):
        """delete element based on 3 situations"""
        node = self.lookup(data)
        if node.less is None and node.more is None:
            self.__node_zero_chldrns(node)
        elif node.less is None or node.more is None:
            self.__node_one_chld(node)
        else:
            self.__node_two_chldrns(node)

    @staticmethod
    def __node_zero_chldrns(node):
        """node is listik"""
        parent = node.parent
        if parent.less == node:
            parent.less = None
        else:
            parent.more = None

    @staticmethod
    def __node_one_chld(node):
        """node has one child"""
        parent = node.parent
        if node.less is not None:
            child_node = node.less
        else:
            child_node = node.more

        if parent.less == node:
            parent.less = child_node
        else:
            parent.more = child_node

    def __node_two_chldrns(self, node):
        """node has 2 childrens"""
        parent = node.parent
        listik = self.__find_next_listik(node)
        data = listik.data
        self.__node_zero_chldrns(listik)
        listik_node = Node(data)
        listik_node.less, listik_node.more = node.less, node.more

        if parent.less == node:
            parent.less = listik_node
        else:
            parent.more = listik_node

    def __find_next_listik(self, node):
        """get listik node"""
        if node.less is not None:
            return self.__find_next_listik(node.less)
        elif node.more is not None:
            return self.__find_next_listik(node.mode)
        else:
            return node
