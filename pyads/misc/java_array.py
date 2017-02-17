# -*- coding: utf-8 -*-

class Array:
    """Array object, behaves like a Java array."""
    def __init__(self, dimension=1, *size):
        if len(size) != dimension:
            raise self.ArraySizeMissingException()

        if size[0] < 0:
            raise self.NegativeArraySizeException()

        if dimension < 1:
            raise self.DimensionsOutOfBoundsException()
        elif dimension > 1:
            # Populate arrays with other arrays until bottom dimension is reached.
            self._container = [Array(dimension - 1, *size[:dimension - 1]) for index in range(size[0])]
        else:
            self._container = [None] * size[0]

    def __getitem__(self, key):
        """Defines indexed getting behaviour for objects of this class."""
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
        if isinstance(self._container[0], Array):
            raise self.ArrayDimensionException()
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


    class NegativeArraySizeException(Exception):
        pass


    class DimensionsOutOfBoundsException(Exception):
        pass


    class ArraySizeMissingException(Exception):
        pass


    class ArrayDimensionException(Exception):
        pass

if __name__ == '__main__':
    arr = Array(2, 10, 10)

    for x in range(10):
        for y in range(10):
            arr[x][y] = (x,y)

    for x in arr:
        print x
