'''
Elliot Williams
08/03/18
2.1
Q: `Remove Dups`: Write code to remove duplicates from an unsorted linked list
'''

class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + "->" + str(self.next)

def removeDuplicates(head):

    # Edge case of empty input LinkedList
    if head == None:
        return None

    globalHead = head
    values = set()

    # Iterates over LinkedList, looking for duplicates
    i = 0
    while head != None:
        new_val = head.value
        if new_val not in values:
            values.add(new_val)
            phead = head
        else:
            phead.next = head.next # skips duplicated value

        head = head.next

    print(globalHead)
    return globalHead

list1 = (LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None)))))
list2 = (LinkedList(1, LinkedList(1, LinkedList(2, LinkedList(1, LinkedList(2, None))))))
list3 = (LinkedList(1, LinkedList(1, LinkedList(1, LinkedList(1, None)))))


assert str(removeDuplicates(list3)) == "1->None"
assert str(removeDuplicates(list1)) == "1->2->3->4->None"
assert str(removeDuplicates(list2)) == "1->2->None"

'''
Should try to redo this one in a bit

--- had issues with implementing it with the end node

Time Complexity: O(N)
Space Complexity: O(K), in which K is the number of unique values
'''
