'''
Elliot Williams
08/03/18
2.5
Q: `Sum Lists` : You have two numbers represented by a linked list, where each
   node contains a single digit. The digits are stored in reverse order, such
   that the 1's digit is at the head of the list. Write a function that adds the
   two numbers and returns the sum as a linked list.
'''

class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + "->" + str(self.next)

import math

def sumListRev(head1, head2):

    print(">>>>")
    print(head1)
    print(head2)
    print("----")

    # Figures out which of the input linked lists are the longest
    if getLength(head1) > getLength(head2):
        curr_long  = head1
        curr_short = head2
    else:
        curr_long  = head2
        curr_short = head1
    long_head = curr_long

    print(curr_short)
    print(curr_long)
    print("vvvv")

    carry = 0
    while curr_long != None:

        short_val = 0
        if curr_short:
            short_val = curr_short.value

        print("Carry:{} , Short Val:{}, Long Val: {}".format(carry, short_val, curr_long.value))

        # Calculates the 'current' sum up to the given decimal place
        curr_sum = curr_long.value + short_val + carry
        print("Curr_Sum: {}".format(curr_sum))

        # Calculates the appropriate node value, and carry value
        curr_long.value = curr_sum % 10
        carry = math.floor(curr_sum / 10)

        # Deals with edge cases, and going to the next decimal place in
        # preparation for the next loop
        if curr_short:
            curr_short = curr_short.next
        if not curr_long.next and carry > 0:
            curr_long.next = LinkedList(carry, None)
            carry = 0
        curr_long = curr_long.next

    print(long_head)
    return long_head

def getLength(head):
    curr_len = 0
    while head != None:
        curr_len += 1
        head = head.next
    return curr_len

list1 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None)))))
list2 = (LinkedList(1, LinkedList(1, LinkedList(1, LinkedList(1, None)))))
list3 = (LinkedList(9, LinkedList(9, LinkedList(9, LinkedList(9, None)))))

assert str(sumListRev(list1, list2)) == "2->3->4->5->None"

list2 = (LinkedList(1, LinkedList(1, LinkedList(1, LinkedList(1, None)))))
list3 = (LinkedList(9, LinkedList(9, LinkedList(9, LinkedList(9, None)))))

assert str(sumListRev(list2, list3)) == "0->1->1->1->1->None"

#  Time Complexity: O(max(N,M))
# Space Complexity: O(1)

'''
This was totally correct!
'''
