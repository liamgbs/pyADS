# -*- coding: utf-8 -*-

class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            self.root = self._Node(None, data)

    def get_size(self):
        """Return number of items in list."""
        if self.root is None:
            return 0
        else:
            return self.root.get_size()

    def get_item(self, index):
        """Return item at index specified and remove it."""
        if index == 0:
            self.get_first_item()
        else:
            return self.root.get_item(index)

    def get_first_item(self):
        """Return first item in list and remove it."""
        if self.root is None:
            raise ListEmptyError()
        else:
            data = self.root.data
            self.root = self.root.next_node
            return data

    def get_last_item(self):
        """Return last item in list and remove it."""
        if self.root is None:
            raise ListEmptyError()

        if self.root.next_node is None:
            data = self.root.data
            self.root = None
            return data
        else:
            return self.root.get_last_item()

    def peek_item(self, index):
        """Return item at index but do not remove it."""
        if index == 0:
            if self.root is None:
                raise IndexError("List is empty.")
            else:
                return self.root.data
        else:
            return self.root.peek_item(index)

    def peek_first_item(self):
        """Return first item but do not remove it."""
        if self.root is None:
            raise ListEmptyError()
        else:
            return self.root.data

    def peek_last_item(self):
        """Return last item but do not remove it."""
        if self.root is None:
            raise ListEmptyError()
        else:
            return self.root.peek_last_item()

    def add_item(self, data, index):
        """Insert item at index."""
        if index == 0:
            add_item_front(data)
        else:
            return self.root.add_item(data, index)

    def add_item_front(self, data):
        """Add item as first element in the list."""
        self.root = self._Node(self.root, data)

    def add_item_end(self, data):
        """Add item as last element in the list."""
        if self.root is None:
            self.add_item_front()
        else:
            self.root.add_item_end()

    def clear(self):
        """Empty list as if newly created."""
        self.root = None

    class _Node:
        def __init__(self, next_node=None, data=None):
            self.next_node = next_node
            self.data = data

        def get_size(self, count=1):
            if self.next_node is None:
                return count
            else:
                return self.next_node.get_size(count+1)

        def get_item(self, index, count=0):
            if index == count+1:
                data = self.next_node.data
                self.next_node = self.next_node.next_node
                return data
            else:
                if self.next_node.next_node is None:
                    raise IndexError()
                else:
                    return self.next_node.get_item(count+1)

        def get_last_item(self):
            if self.next_node.next_node is None:
                data = self.next_node.data
                self.next_node = No

        def add_item(self, data, index):
            raise NotImplementedError()

class ListEmptyError(Exception):
        pass








# Test
if __name__ == '__main__':
    x = LinkedList()
    x.add_item_front("world")
    x.add_item_front("hello")
    print x.get_item(1)
    print x.peek_first_item()
    print x.get_size()
