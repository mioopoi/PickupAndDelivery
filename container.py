"""
Date of creation: 2016/12/11

Description: This module contains the customized container used in this project.

"""


import collections
import heapq


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class _LinkedListNode:
    """
    Class for a node in the LinkedList.
    """
    def __init__(self, data, next_node=None, prev_node=None):
        """
        Initialize a node.
        :param data: instance variable to store the data
        :param next_node: instance variable with address of next node
        :param prev_node: instance variable with address of previous node
        :type next_node: _LinkedListNode
        :type prev_node: _LinkedListNode
        :return:
        """
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data


class LinkedList:
    """
    Class for a circular, doubly linked list with a sentinel.

    Please access "http://www.cs.dartmouth.edu/~cs1/chapter19/" for more details.

    """
    def __init__(self):
        """
        Create the sentinel node, which is before the first node and after the last node.
        :return: None
        """
        self.sentinel = _LinkedListNode(None)
        self.sentinel.next_node = self.sentinel
        self.sentinel.prev_node = self.sentinel

    def __str__(self):
        """
        Return a string representation of a circular, doubly linked list with a sentinel
        :return: str
        """
        s = "["

        x = self.sentinel.next_node
        while x != self.sentinel:
            if type(x.data) == str:
                s += "'"
            s += str(x.data)
            if type(x.data) == str:
                s += "'"
            if x.next_node != self.sentinel:
                s += ", "  # if not the last node, add the comma and space
            x = x.next_node

        s += "]"
        return s

    def first_node(self):
        """
        Return a reference to the first node in the list, if there is one.
        If the list is empty, return None.
        :return: the first node in the list
        """
        if self.sentinel.next_node == self.sentinel:
            return None
        else:
            return self.sentinel.next_node

    def insert_after(self, x, data):
        """
        Insert a new node after node x.
        :param x: the node that the new node will insert after
        :type x: _LinkedListNode
        :return: None
        """
        new_node = _LinkedListNode(data)  # make a new _LinkedListNode object.

        new_node.prev_node = x
        new_node.next_node = x.next_node

        x.next_node = new_node

        new_node.next_node.prev_node = new_node

    def append(self, data):
        """
        Insert a new node at the end of the list.
        :return: None
        """
        last_node = self.sentinel.prev_node
        self.insert_after(last_node, data)

    def prepend(self, data):
        """
        Insert a new node at the start of the list.
        :return: None
        """
        self.insert_after(self.sentinel, data)

    def remove(self, x):
        """
        Delete node x from the list.
        :param x: instance variable with address of the node to be deleted
        :type x: _LinkedListNode
        :return: None
        """
        x.prev_node.next_node = x.next_node
        x.next_node.prev_node = x.prev_node

    def find(self, data):
        """
        Find a node containing data, and return a reference to it.
        If no node contains data, return None.
        :param data: instance variable to store the data
        :return: the reference of the found node
        """

        # Trick: Store a copy of the data in the sentinel, so that the data is always found.
        self.sentinel.data = data

        x = self.first_node()
        while x.data != data:
            x = x.next_node

        # Restore the sentinel's data.
        self.sentinel.data = None

        # Why did we drop out of the while-loop?
        # If we found the data in the sentinel, then it wasn't anywhere else in the list.
        if x == self.sentinel:
            return None    # data wasn't really in the list
        else:
            return x       # we found it in x, in the list


def test_linked_list():
    l = LinkedList()
    l.append("Maine")
    l.append("Idaho")
    l.append("Utah")
    print l

    # Add Ohio after Idaho.
    node = l.find("Idaho")
    if node is not None:
        print(node.get_data())
        l.insert_after(node, "Ohio")
    print l

    # Delete Idaho
    if node is not None:
        l.remove(node)
    print l

    # Empty out the list, one node at a time.
    while l.first_node() is not None:
        l.remove(l.first_node())
    print l


if __name__ == '__main__':
    test_linked_list()