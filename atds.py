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

def main():
    q = Queue()
    q.enqueue("Roy")
    q.enqueue("Patrick")
    print(q)
    q.dequeue()
    print(q)

if __name__ == "__main__":
    main()
