from data_structures.linked_list import LinkedList
import ctypes
"""hashtable realisation without build-in structures"""


class Node:
    """custom node with specific data"""
    def __init__(self, key, key_hash, value):
        self.key = key
        self.key_hash = key_hash
        self.value = value
        self.next = None
        self.prev = None


class LlinkedList(LinkedList):
    """custom Linked list realisation"""
    def __init__(self):
        super(LlinkedList, self).__init__()

    def insert_node_before(self, node, insert_node):
        """insert node before specific one"""
        start = self.head
        while start:
            if start.next == node:
                insert_node.next = node
                insert_node.prev = start
                node.prev = insert_node
                start.next = insert_node
                break
            start = start.next

    def append(self, data):
        """add element to the end of linked list"""
        new_node = data
        if self.head:
            current_node = self.head
            while current_node:
                if current_node.next is None:
                    current_node.next = new_node
                    new_node.prev = current_node
                    break
                else:
                    current_node = current_node.next
        else:
            new_node.prev = self.head
            self.head = new_node


class HashTable:
    """hash table class"""
    def __init__(self, arr_len: int, hash_str_len):
        self.__llist = LlinkedList()
        self.__hash_str = ' ' * hash_str_len * arr_len
        self.__hash_str_len = hash_str_len

    def get__hash_str(self):
        """get private hash string"""
        return self.__hash_str

    def insert(self, key, value):
        """Insert element"""
        hashed_key = self.hash(key)
        new_node = Node(key, hashed_key, value)
        id_new_node = id(new_node)
        if self.__is_empty(hashed_key):
            self.__insert_id_to_str(hashed_key, id_new_node)
            self.__llist.append(new_node)
        else:
            link_to_collision_node_id = self.__get_id_by_hash(hashed_key)
            link_to_collision_node = self.__get_obj_by_id(link_to_collision_node_id)
            self.__llist.insert_node_before(link_to_collision_node, new_node)
            self.__insert_id_to_str(hashed_key, id_new_node)

    def lookup(self, key):
        """return value by key"""
        hashed_key = self.hash(key)
        item = self.__get_id_by_hash(hashed_key)
        node = self.__get_obj_by_id(item)
        if node.key == key:
            return node.value
        else:
            start = node
            while start:
                if start.key == key:
                    return start.value
                else:
                    start = start.next

    def get_node_by_hash(self, key):
        """return link to node by hash"""
        hashed_key = self.hash(key)
        item = self.__get_id_by_hash(hashed_key)
        node = self.__get_obj_by_id(item)
        if node.key == key:
            return node
        else:
            start = node
            while start:
                if start.key == key:
                    return start
                else:
                    start = start.next

    def delete(self, key):
        """delete node from hash str and hashtable"""
        node = self.get_node_by_hash(key)
        parent = node.prev
        son = node.next
        if parent:
            parent.next = son
        else:
            self.__llist.head = son

        hkey = self.hash(key)
        empty_key = ' ' * self.__hash_str_len
        self.__insert_id_to_str(hkey, empty_key)

    @staticmethod
    def hash(item):
        """my hash function"""
        if isinstance(item, (str, int, tuple)):
            summ = 0
            for i in str(item):
                summ += id(i)
            return summ % 30
        else:
            raise TypeError

    def __is_empty(self, hashed_key):
        """check for collision"""
        val = self.__get_id_by_hash(hashed_key)
        if val:
            return False
        else:
            return True

    def __insert_id_to_str(self, hashed_key, item_id):
        """add link to node into hash string on hashed_key place"""
        left_str_part = self.__hash_str[0:hashed_key * self.__hash_str_len]
        middle_str_part = self.fix_item_id_len(item_id)
        right_str_part = self.__hash_str[(hashed_key+1) * self.__hash_str_len:]
        tmp_str = str(left_str_part) + str(middle_str_part) + str(right_str_part)
        self.__hash_str = tmp_str

    def fix_item_id_len(self, item_id):
        """If link to node < element size - ajust"""
        tmp = ' ' * self.__hash_str_len
        if len(str(item_id)) < self.__hash_str_len:
            new_str = str(item_id) + tmp[len(str(item_id)):]
            return new_str

    def __get_id_by_hash(self, key_hash):
        """get element from our hash string"""
        return self.__hash_str[self.__hash_str_len * key_hash:self.__hash_str_len * (key_hash+1)].replace(' ', '')

    @staticmethod
    def __get_obj_by_id(item_id):
        """get object by id"""
        return ctypes.cast(int(item_id), ctypes.py_object).value
