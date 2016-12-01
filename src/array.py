class Array:
    """Array object, behaves like a Java array."""
    def __init__(self, size):
        self._container = [None]*size

    def __getitem__(self, key):
        """Defines indexed setting behaviour for objects of this class."""
        if key > len(self._container) - 1:
            raise self.ArrayOutOfBoundsException()
        elif self._container[key] is None:
            raise self.NonePointerException()
        else:
            return self._container[key]

    def __setitem__(self, key, data):
        """Defines indexed setting behaviour for objects of this class."""
        if key > len(self._container) - 1:
            raise self.ArrayOutOfBoundsException()
        else:
            self._container[key] = data

    def __iter__(self):
        self._iter_index = 0
        return self

    def next(self): # __next__ if python3
        """Defines behaviour for iterating over objects of this class."""
        if self._iter_index == self.length():
            raise StopIteration

        if self._container[self._iter_index] is None:
            raise self.NonePointerException()
        else:
            self._iter_index += 1
            return self._container[self._iter_index - 1]

    def length(self):
        """Returns maximum capacity of the array."""
        return len(self._container)


    class ArrayOutOfBoundsException(Exception):
        pass


    class NonePointerException(Exception):
        pass
