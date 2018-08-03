'''
Elliot Williams
08/03/18
2.3
Q: `Delete Middle Node`: Implement an algorithm to find the kth to last element
   of a singly linked list
'''

class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + "->" + str(self.next)

def deleteMiddle(midd_node):

    assert midd_node.next != None

    midd_node.value = midd_node.next.value
    midd_node.next  = midd_node.next.next

    return midd_node

# Time  Complexity: O(1)
# Space Complexity: O(1)

'''
This was incorrectly implemented, and I didn't deal with the edge case.
'''
