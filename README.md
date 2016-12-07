# pyADS
Implementations of algorithms and datastructures in python.

This repository houses my Python implementations of some data structures as well
as some accompanying algorithms, they are to prove to myself and to showcase my
own understanding of the concepts. None are meant to be used in production
(although feel free to do so) and might not be the best solutions.

## Array

The array implementation is designed to behave like a Java array and have similar
syntax as far as python will allow. An Array object is iterable only if one
dimensional.

```python
# Define a 2 dimensional array with each dimesion of size 10.
arr = Array(2, 10, 10)

# Assign a value to the array.
arr[0][5] = "hello"

# Get a value from the array.
print arr[0][5]
```

###### TODO:

* Allow iterating through multiple dimensions.
* Implement sorting.
