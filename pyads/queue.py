# -*- coding: utf-8 -*-

from singly_linked_list import SinglyLinkedList

class Queue:
    def __init__(self, capacity=float("inf")):
        self._queue = []
        self._capacity = capacity

    def enqueue(self, data):
        if self.get_size() < self._capacity:
            self._queue.insert(0, data)
        else:
            raise OverflowError()

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self._queue.pop(0)

    def peek(self):
        return self._queue[0]

    def get_size(self):
        return len(self._queue)

    def get_capacity(self):
        return self._capacity

    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False


class LinkedListQueue:
    def __init__(self, capacity=float("inf")):
        self._queue = SinglyLinkedList()
        self._capacity = capacity

    def enqueue(self, data):
        if self.get_size() < self._capacity:
            self._queue.add_item_end(data)
        else:
            raise OverflowError()

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self._queue.get_first_item()

    def peek(self):
        return self._queue.peek_first_item()

    def get_size(self):
        return self._queue.get_size()

    def get_capacity(self):
        return self._capacity

    def is_empty(self):
        return self._queue.is_empty()

class OverflowError(Exception):
    pass

ll = Queue(6)
ll.enqueue(1)
ll.enqueue(1)
ll.enqueue(1)
ll.enqueue(1)
ll.enqueue(1)
print ll.get_capacity()
print ll.get_size()
ll.dequeue()
print ll.get_size()


for x in range(10):
    print ll.dequeue()
