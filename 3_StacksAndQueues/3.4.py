'''
Elliot Williams
09/04/18
3.4
Q: `Queue via Stacks': Implement a MyQueue class which implements a queue using
two stacks
'''

from stack_queue_implementation import *

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def add(self, item):
        # Removes all items from stack1, put into stack2 in reverse order
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())

        # Pushes the item being added to MyQueue onto the bottom of stack1
        self.stack1.push(item)

        # Puts back all items in stack2 back to stack1
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())

    def pop(self):
        if self.isEmpty():
            raise Exception("MyQueue is Empty!")

        return self.stack1.pop()

    def peek(self):
        return self.stack1.peek()

    def isEmpty(self):
        return self.stack1.isEmpty()


mq = MyQueue()
mq.add(1)
mq.add(2)
mq.add(3)
mq.add(0)
mq.add(15)
mq.add(300)
assert mq.pop() == 1
assert mq.peek() == 2
assert mq.pop() == 2
assert mq.pop() == 3
assert mq.peek() == 0
assert mq.pop() == 0
assert mq.pop() == 15
assert mq.pop() == 300
