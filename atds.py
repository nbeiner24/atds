#!/usr/bin/env python3

"""
atds.py
This program stores different types of data structures, such as a Stack.
"""

__author__ = "Nicolas Beiner"
__version__ = "2024-02-13"

class Stack(object):

    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, thing):
       self.stack.append(thing)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return None

    def size(self):
        return len(self.queue)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def __repr__(self):
        return str(self.queue)

class Deque(object):

    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.append(item)

    def add_rear(self, item):
        self.deque.insert(0, item)

    def remove_front(self):
        return self.deque.pop()

    def remove_rear(self):
        return self.deque.pop(0)

    def size(self):
        return len(self.deque)

    def is_empty(self):
        if len(self.deque) == 0:
            return True
        else:
            return False
        
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next
    
    def __repr__(self):
        return "Node[data=" + str(self.data) + ", next=" + str(self.next) + "]"

class UnorderedList(object):
    """Defines an unordered (unsorted) list"""
    def __init__(self):
        self.head = None

    def add(self, new_data):
        temp_node = Node(new_data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def length(self):
        node_count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            node_count += 1
        return node_count
    
    def search(self, data):
        i = self.head
        while (i != None):
            if (i.get_data() == data):
                return True
            else:
                return False
        return False

    def remove(self, data):
        prev = None
        current = self.head
        while (current != None):
            if (current.get_data() == data):
                if (prev == None):
                    self.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                return
            else:
                prev = current
                current = current.get_next()

    def __repr__(self):
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        if result[-1] == ",":
            result = result[:-1] # remove trailing comma
        result = result + "]"
        return result

def main():
    n = Node(3)
    n2 = Node(5)
    n.set_next(n2)
    print(n)

if __name__ == "__main__":
    main()
