'''
Elliot Williams
08/03/18
2.2
Q: `Return Kth to Last`: Implement an algorithm to find the kth to last element
   of a singly linked list
'''

class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + "->" + str(self.next)

def getKthToLast(head, k):
    assert head is not None
    assert k >= 0
    head_len = getLength(head)
    node_index = head_len - k - 1

    i = 0
    while i != node_index:
        head = head.next
        i += 1

    return head

def getLength(head):
    curr_len = 0
    while head != None:
        curr_len += 1
        head = head.next
    return curr_len

list1 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None)))))
list2 = (LinkedList(1, LinkedList(1, LinkedList(2, LinkedList(1, LinkedList(2, None))))))
list3 = (LinkedList(1, LinkedList(1, LinkedList(1, LinkedList(1, None)))))

assert getKthToLast(list1, 2).value == 2
assert getKthToLast(list2, 0).value == 2
assert getKthToLast(list2, 3).value == 1

# Time  Complexity: O(N)
# Space Complexity: O(1)
# This one was perfect :)
