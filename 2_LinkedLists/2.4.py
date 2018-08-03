'''
Elliot Williams
08/03/18
2.4
Q: `Partition` : Write code to partition a linked list around a value x, such
   that all nodes less than x come before all nodes greater than or equal to x.
   If x is contained within the list, the values of x only need to be after the
   elements less than x.
'''

class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + "->" + str(self.next)

# Assumption: both the smaller and bigger segments of the linked list are O(N)
# ... so, there is no asymptotic space cost to store two linked listsself.
# Otherwise, we could only store one additional linked list for the O(1)
# portion, which would reduce space complexity provided the assumption is true.

def partitionLinkedList(head, partition_value):

    # Defines pointers for two linked lists corresponding to the partition
    curr_small = None
    curr_big   = None
    small_head = None
    big_head   = None

    # Partitions the input linked list into two sub-linked lists
    while head != None:
        if head.value < partition_value:
            if small_head == None:
                small_head = LinkedList(head.value, None)
                curr_small = small_head
            else:
                curr_small.next = LinkedList(head.value, None)
                curr_small = curr_small.next
        else:
            if big_head == None:
                big_head = LinkedList(head.value, None)
                curr_big = big_head
            else:
                curr_big.next = LinkedList(head.value, None)
                curr_big = curr_big.next

        head = head.next

    # Returns the partitioned linked lists ligated together into one
    if small_head == None:
        return big_head
    else:
        curr_small.next = big_head
        return small_head

list1 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None)))))
list2 = (LinkedList(1, LinkedList(1, LinkedList(1, LinkedList(1, None)))))
list3 = (LinkedList(4, LinkedList(3, LinkedList(2, LinkedList(1, None)))))
list4 = (LinkedList(1, LinkedList(2, LinkedList(1, LinkedList(2, None)))))

assert str(partitionLinkedList(list1, 3)) == "1->2->3->4->None"
assert str(partitionLinkedList(list2, 1)) == "1->1->1->1->None"
assert str(partitionLinkedList(list3, 3)) == "2->1->4->3->None"
assert str(partitionLinkedList(list4, 2)) == "1->1->2->2->None"

#  Time Complexity: O(N)
# Space Complexity: O(N)

'''
There was a asmall issue -- line 49 was missing before
'''
