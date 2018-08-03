'''
Elliot Williams
08/03/18
2.6
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
def isPalindrome(head):
    N = getLength(head)
    values = []

    # Adds the first half of the linked list to an array
    for i in range(math.floor(N/2)):
        values.append(head.value)
        head = head.next

    # Skips the middle value (irrelevant if it exists for palindrome status)
    if N % 2 == 1:
        head = head.next

    # The second half of the values should be to the first half played backwards
    for i in reversed(range(math.floor(N/2))):
        if head.value != values[i]:
            return False
        head = head.next
    return True

def getLength(head):
    curr_len = 0
    while head != None:
        curr_len += 1
        head = head.next
    return curr_len

list1 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None)))))
list2 = (LinkedList(1, LinkedList(1, LinkedList(1, LinkedList(1, None)))))
list3 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(2, LinkedList(1, None))))))

assert not isPalindrome(list1)
assert isPalindrome(list2)
assert isPalindrome(list3)

#  Time Complexity: O(N)
# Space Complexity: O(N)

'''
Perfect first run!
'''
