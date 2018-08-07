class MinStackNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class MinStack:
    def __init__(self):
        self.top = None # Of type StackNode
        self.min = None

    def push(self,data):
        if self.top == None:
            self.min = MinStackNode(data, None)
            self.top = MinStackNode(data, None)
        else:
            self.top = MinStackNode(data, self.top)
            if data <= self.min.data:
                self.min = MinStackNode(data, self.min)

    def pop(self):
        if self.top == None:
            raise Exception("Empty Stack is Empty")
        else:
            data = self.top.data
            self.top = self.top.next
            if data == self.min.data:
                self.min = self.min.next
            return data

    def peek(self):
        if self.top == None:
            raise Exception("Empty Stack can't be peeked")
        return top.data

    def isEmpty(self):
        return top == None

    def getMin(self):
        if self.min == None:
            return None
        else:
            return self.min.data

ms = MinStack()
ms.push(1)
ms.push(2)
ms.push(3)
assert ms.getMin() == 1
ms.push(0)
assert ms.getMin() == 0
assert ms.pop() == 0
assert ms.getMin() == 1
assert ms.pop() == 3
assert ms.pop() == 2
assert ms.pop() == 1
assert ms.getMin() == None
