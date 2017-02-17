# pyADS
Implementations of algorithms and datastructures in Python.

This repository houses my Python implementations of some data structures as well
as some accompanying algorithms, they are to prove to myself and to showcase my
own understanding of the concepts. None are meant to be used in production
(although feel free to do so) and might not be the best solutions.

All implementations are done with nothing but the python built in types and
lower level data structures found within this project.

Please don't use my code to do your homework.

## Linked Lists

A linked list is a data structure where data is held within nodes. Each node
holds a reference to the next and to traverse it you must start at the root and
move across nodes until you get to where you want.

### Singly Linked List

A singly linked list holds only one reference to the next node in the list.

```python
# Define a new linked list
linkedlist = SinglyLinkedList()

# Add some data
linkedlist.add_item_front(1)
linkedlist.add_item_front(2)
linkedlist.add_item_front(3)

# Peek at the data but dont remove it from list
print linkedlist.peek_first_item()
>> 3

# Peek at a specified index
print linkedlist.peek_item(1)
>> 2

# Get the data and remove it from list
print linkedlist.get_last_item()
>> 1

# Get size of list
print linkedlist.get_size()
>> 2

# Empty the list
linkedlist.clear()
```

## Stacks

A stack is a last in first out data structure, data pushed to the stack can be
retrived by popping immediately, to get to the first peice of data pushed, one must
pop until the bottom of the stack is reached. Stacks are useful with jobs that
require back tracking such as a function call stack or checking for balanced parentheses.

### Stack

The stack is has an default capacity of infinity, but this can be set upon
instantiation. Pushing beyond the stacks capacity will cause a `StackOverflowError`.
However popping an empty stack will return `None`.

```python
# Define a stack with a capacity of 3 elements
my_stack = Stack(3)

# Push some data to the stack
my_stack.push("world!")
my_stack.push("Hello, ")

# Get size of stack
print my_stack.get_size()
>> 2

# Pop data from stack
print my_stack.pop() + my_stack.pop()
>> "Hello, world!"
```

## Miscellaneous

### Java Array

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
>> "hello"
```
