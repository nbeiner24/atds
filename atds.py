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
