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
                i = i.get_next()
        return False

    def remove(self, data):
        prev = None
        current = self.head
        while (current != None and self.head != None):
            if (current.get_data() == data):
                if (prev == None):
                    self.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
            else:
                prev = current
            current = current.get_next()

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def append(self, item):
        temporary = Node(item)
        current = self.head
        while (current.get_next() != None):
            current = current.get_next()
        current.set_next(temporary)

    def index(self, item):
        i_count = 0
        if (self.head == None):
            return None
        current = self.head
        while (current != None):
            if (current.get_data() == item):
                break
            current = current.get_next()
            i_count += 1
        if current == None:
            return None
        else:
            return i_count

    def insert(self, pos, item):
        temporary = Node(item)
        index = 0
        current = self.head
        prev = None
        while index < pos:
            prev = current
            current = current.get_next()
            index += 1
        if index == 0:
            temporary.set_next(current)
            self.head = temporary
        else:
            prev.set_next(temporary)
            temporary.set_next(current)

    def pop(self, i = -1):
        if self.head == None:
            return None
        if i == -1:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            result = current.get_data()
            previous.set_next(None)
            return result
        elif i == 0:
            current = self.head
            result = current.get_data()
            self.head = current.get_next()
            return result
        else:
            current = self.head
            previous = None
            position = 0
            while position < i:
                previous = current
                current = current.get_next()
                position += 1
            result = current.get_data()
            previous.set_next(current.get_next())
            return result

    def __repr__(self):
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        if result[-1] == ",":
            result = result[:-1] # remove trailing comma
        result = result + ",]"
        return result

class UnorderedListStack(object):

    def __init__(self):
        self.stack = UnorderedList()

    def pop(self):
        return self.stack.pop(0)

    def push(self, thing):
       self.stack.add(thing)
    
    def peek(self):
        val = self.stack.pop(0)
        self.stack.add(val)
        return val
        
    def size(self):
        return self.stack.length()
    
    def is_empty(self):
        return self.stack.is_empty()

class HashTable():

    def __init__(self, m):
        self.size = m
        self.keys = [None] * m
        self.values = [None] * m

    def put(self, key, value):
        hashval = key % self.size
        if self.keys[hashval] == None:
            self.keys[hashval] = key
            self.values[hashval] = value
        elif self.keys[hashval] == key:
            self.values[hashval] = value    
        else:
            nextkey = (hashval + 1) % self.size  
            while self.keys[nextkey] != None and \
                  self.keys[nextkey] != key:
                nextkey = (nextkey + 1) % self.size
            if self.keys[nextkey] == key:
                self.values[nextkey] = value
            else:
                self.keys[nextkey] = key
                self.values[nextkey] = value

    def get(self, key):
        hashval = key % self.size
        while self.keys[hashval] != None and self.keys[hashval] != key:
            hashval += 1
        if self.keys[hashval] == key:
            return self.values[hashval]
        else:
            return None
    
    def __repr__(self):
        return ("Keys:   " + str(self.keys) + "\n" + "Values: " + str(self.values))
    
class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_root_val(self):
        return self.val
    
    def set_root_val(self, new_val):
        self.val = new_val

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right
    
    def insert_left(self, val):
        new_subtree = BinaryTree(val)
        new_subtree.left = self.left
        self.left = new_subtree

    def insert_right(self, val):
        new_subtree = BinaryTree(val)
        new_subtree.right = self.right
        self.right = new_subtree

    def __repr__(self):
        return "BinaryTree[key=" + str(self.val) + \
               ",left_child=" + str(self.left) + \
               ",right_child=" + str(self.right) + "]"

def main():
    n = Node(3)
    n2 = Node(5)
    n.set_next(n2)
    print(n)

if __name__ == "__main__":
    main()
