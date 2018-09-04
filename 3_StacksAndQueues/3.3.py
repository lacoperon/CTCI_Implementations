'''
Elliot Williams
09/04/18
3.3
Q: `Stack of Plates': Imagine a stack of plages; if the stack gets too high,
it might topple. So, implement a data structure `SetOfStacks` that mimics this.
It should be composed of several stacks, and create a new stack once the
previous one exceeds capacity.
'''

from stack_queue_implementation import *

class SetOfStacks:

    def __init__(self, max_size=5):
        self.stacks = [Stack()]
        self.curr_stack_index = 0
        self.max_size = max_size

    def isEmpty(self):
        return (self.curr_stack_index == 0 and self.stacks[0].isEmpty())

    def peek(self):
        if self.isEmpty():
            raise Exception("SetOfStacks is Empty")

        if self.stacks[self.curr_stack_index].isEmpty():
            return self.stacks[self.curr_stack_index-1].peek()

        return self.stacks[self.curr_stack_index].peek()

    def push(self, item):
        self.stacks[self.curr_stack_index].push(item)
        if self.stacks[self.curr_stack_index].size >= self.max_size - 1:
            self.stacks.append(Stack())
            self.curr_stack_index += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("SetOfStacks is Empty")

        if self.stacks[self.curr_stack_index].isEmpty():
            self.curr_stack_index -= 1
            self.stacks = self.stacks[:len(self.stacks)-1]

        return self.stacks[self.curr_stack_index].pop()

ms = SetOfStacks()
ms.push(1)
ms.push(2)
ms.push(3)
ms.push(0)
ms.push(15)
ms.push(300)
assert ms.pop() == 300
assert ms.peek() == 15
assert ms.pop() == 15
assert ms.pop() == 0
assert ms.peek() == 3
assert ms.pop() == 3
assert ms.pop() == 2
assert ms.pop() == 1
