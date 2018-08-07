
class StupidArrayStack:
    def __init__(self, stack_length, num_stacks=3):
        self.array = (num_stacks * stack_length) * [None]
        self.top_index = [i * stack_length for i in range(num_stacks)]
        self.stack_length = stack_length
        
    def pop(self, stack_num):
        top_index = self.top_index[stack_num]
        top = self.array[top_index]

        if top == None and top_index == stack_num * self.stack_length:
            raise Exception("Stack {} is Empty".format(stack_num))
        else:
            self.array[top_index] = None
            if top_index != stack_num * self.stack_length:
                self.top_index[stack_num] -= 1
            return top

    def peek(self, stack_num):
        top_index = self.top_index[stack_num]
        top = self.array[top_index]

        if top == None and top_index == stack_num * stack_length:
            raise Exception("Stack {} is Empty".format(stack_num))
        else:
            return top


    def add(self, item, stack_num):
        top_index = self.top_index[stack_num]
        top = self.array[top_index]

        if top == None and top_index == stack_num * self.stack_length:
            self.array[top_index] = item
        elif top_index == (stack_num + 1) * self.stack_length - 1:
            raise Exception("Stack {} is Full".format(stack_num))
        else:
            self.array[top_index + 1] = item
            self.top_index[stack_num] += 1

ss = StupidArrayStack(3)
ss.add(1, 0)
ss.add("a",1)
ss.add(2, 0)
ss.add("b",1)
ss.add(3, 0)
ss.add("c",1)
# ss.add(4, 0)

assert ss.pop(0) == 3
assert ss.pop(1) == "c"
assert ss.pop(0) == 2
assert ss.pop(1) == "b"
assert ss.pop(0) == 1
assert ss.pop(1) == "a"
