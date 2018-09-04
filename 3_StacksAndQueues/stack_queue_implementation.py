class StackNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None # Of type StackNode
        self.size = 0

    def pop(self):
        if self.top == None:
            raise Exception("Empty Stack can't be popped")
        popped_item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_item

    def push(self,data):
        new_node = StackNode(data, self.top)
        self.top = new_node
        self.size += 1

    def peek(self):
        if self.top == None:
            raise Exception("Empty Stack can't be peeked")
        return self.top.data

    def isEmpty(self):
        return self.top == None

    def toArray(self):
        tmp = self.top
        array = []
        while self.top != None:
            array.append(self.top.data)
            self.top = self.top.next
        self.top = tmp
        return array


class QueueNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None

    def add(self, item):
        node = QueueNode(data, None)
        if self.isEmpty():
            self.top = node
            self.bottom = node
        else:
            self.bottom.next = node
            self.bottom = node

    def remove(self):
        if self.isEmpty():
            raise Exception("Empty Queue can't be asked for data")
        else:
            first_data = self.top.data
            # Edge case in which the only node is being removed
            if self.top == self.bottom:
                self.bottom = None
            self.top = self.top.next
            return first_data

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty Queue can't be asked for data")
        else:
            return self.top.data

    def isEmpty(self):
        return self.top == None and self.bottom == None
