# -*- coding: utf-8 -*-
class Stack:
    def __init__(self, capacity=float("inf")):
        self._stack = []
        self.capacity = capacity

    def push(self, data):
        if self.get_size() < self.capacity:
            self._stack.append(data)
        else:
            raise StackOverflowError()

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def get_size(self):
        return len(self._stack)

    def get_capacity(self):
        return self.capacity

    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False

class StackOverflowError(Exception):
    pass
