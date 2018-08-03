'''
Elliot Williams
08/03/18
2.5
Q: `Loop Detection': Given a circular linked list, implement an algorithm that
   returns the beginning of the loop.
'''

class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + "->" + str(self.next)

def detectLoop(head):
    ref_set = set()
    while head != None:
        if head in ref_set:
            return head
        ref_set.add(head)
        head = head.next
    return None


list1 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None)))))
list2 = (LinkedList(1, LinkedList(1, LinkedList(1, LinkedList(1, None)))))

tagged_node = LinkedList(1, None)
list3 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(2, tagged_node)))))
list4 = (LinkedList(1, list3))
tagged_node.next = list3

assert not detectLoop(list1)
assert not detectLoop(list2)
assert detectLoop(list3)
assert detectLoop(list4)

#  Time Complexity: O(N), where N is the # of nodes until loop. or total length
# Space Complexity: O(N)

'''
Perfect Implementation first try!

Having said that, there's a O(1) space solution if you have a FAST and SLOW
pointer.
'''
