'''
Elliot Williams
09/04/18
3.5
Q: Write a program to sort a stack such that the smallest items are on the top.
You can only use one additional temporary stack, but no other data structures
like arrays. Should support push, pop, peek and isEmpty.
'''

from stack_queue_implementation import *

# Time :  O(N)
# Space:  O(1)
def getMax(stack):
    # Edge case -- there is no max of an empty stack
    # print(stack.toArray())
    assert not stack.isEmpty()

    max = None
    count = None
    tmp = stack.top
    tmpsize = stack.size
    while not stack.isEmpty():
        value = stack.pop()
        if max == value:
            count += 1
        if max == None or value > max:
            max = value
            count = 1

    stack.top = tmp
    stack.size = tmpsize


    return max, count

# Time :  O(N*K), where K is # unique values, or O(N^2) if all unique
# Space:  O(N)
def sortStack(stack):
    orig_size = stack.size
    tempStack = Stack()
    sorted_size = 0

    while tempStack.size < orig_size:
        # Gets curr max value + count, appends to curr sorted stack
        max, count = getMax(stack)
        for i in range(count):
            tempStack.push(max)
        sorted_size += count

        # Push all values but max from stack to tempStack
        while not stack.isEmpty():
            value = stack.pop()
            if value != max:
                tempStack.push(value)

        # Pushes `sorted_size` values from tempStack back to stack
        while tempStack.size > sorted_size:
            stack.push(tempStack.pop())

    return tempStack

stack = Stack()
stack.push(5)
stack.push(1)
stack.push(3)
stack.push(2)
stack.push(4)
# print(stack.top.data)

assert sortStack(stack).toArray() == [1,2,3,4,5]
