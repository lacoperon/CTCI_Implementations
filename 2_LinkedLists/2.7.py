'''
Elliot Williams
08/03/18
2.7
Q: `Intersection` : Given two singly linked lists, determine if the two lists
   intersect. Return the intersecting node. Note that the intersection is
   defined based on reference, not value. That is, if the kth node of the first
   linked list is the exact same node (by ref) as the jth node of the second
   linked list, then they are intersecting.
'''

class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + "->" + str(self.next)

def getLength(head):
    curr_len = 0
    while head != None:
        curr_len += 1
        head = head.next
    return curr_len

def intersect(head1, head2):

    # If you're getting size, you can also get the tail node in the same
    # time complexity, although I suppose this doesnt help asympototic efficiency

    # Figures out which of the two lists are larger and smaller
    if getLength(head1) > getLength(head2):
        cached_list = head2
        searched_list = head1
    else:
        cached_list = head1
        searched_list = head2

    # Caches all nodes in the smaller linked list
    cached_set = cacheRefs(cached_list)

    # Searches the larger linked list for any nodes (by ref) seen in the smaller
    while searched_list != None:
        if searched_list in cached_set:
            return searched_list
        searched_list = searched_list.next
    return None

def cacheRefs(head):
    cached_set = set()
    while head != None:
        cached_set.add(head)
        head = head.next
    return cached_set

list1 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None)))))
list2 = (LinkedList(1, LinkedList(1, LinkedList(1, LinkedList(1, None)))))
list3 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(2, LinkedList(1, None))))))
list4 = (LinkedList(1, list3))

assert not intersect(list1, list2)
assert not intersect(list2, list3)
assert not intersect(list1, list3)
assert intersect(list3, list4)

#  Time Complexity: O(N+M)
# Space Complexity: O(min(N,M))

# An alternative has Time: O(N*M), Space O(1), but I think the former is better

'''
Perfect first time!!!

Having said that, there's an easy optimization -- if there's an intersection,
then the tails must be the same, so we should check that

I added this, but it doesn't help asymptotic time optimization 
'''
