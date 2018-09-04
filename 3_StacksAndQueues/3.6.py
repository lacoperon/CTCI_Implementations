'''
Elliot Williams
09/04/18
3.6
Q: An animal shelter, containing only dogs and cats, operates on a FIFO basis.
People must adopt either the 'oldest' of all the animals (in terms of time at the
shelter), or the 'oldest' of a particular animal. Create a data structure to
maintain this system, and implement `enqueue`, `dequeueAny`, `dequeueDog`,
and `dequeueCat`.
'''

class AnimalLinkedList:
    def __init__(self, data, type, prev=None, next=None, typeNext=None):
        self.data = data
        self.prev = prev
        self.next = next
        self.type = type
        self.typeNext  = typeNext


    def __str__(self):
        return str(self.data) + "->" + str(self.next)

class AnimalShelter:
    def __init__(self):

        # Global head, tail of all animals in shelter
        self.head = None
        self.tail = None

        # Dicts of head, tail node for each animal type
        self.heads = {}
        self.heads['dog'] = None
        self.heads['cat'] = None

        self.tails = {}
        self.tails['dog'] = None
        self.tails['cat'] = None

        # Valid types of animals
        self.types = ['dog', 'cat']

    def __str__(self):
        if not self.head:
            return "EMPTY"

        tmp = self.head
        array = [(tmp.data, tmp.type)]
        while tmp.next:
            tmp = tmp.next
            array.append((tmp.data, tmp.type))

        return str(array)

    def enqueue(self, data, type):
        assert type in self.types

        node = AnimalLinkedList(data, type)
        # Case in which there are no previous animals of `type` in shelter
        if self.heads[type] == None:

            self.heads[type] = node
            self.tails[type] = node

            # Case in which there are no animals at all in shelter
            if self.head == None:
                self.head = node
                self.tail = node

            # There are other animals, just not of `type`
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node

        # Case in which there is at least one animal of `type` in shelter
        # (=> shelter is non-empty)
        else:
            # Sets `node` to be the new tail of `type`
            self.tails[type].typeNext = node
            self.tails[type] = node

            # Sets `node` to be the new global tail of shelter
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def dequeueAny(self):
        if self.head == None:
            raise Exception("Shelter contains no animals")

        # Fetches the first pet in the queue, and gets its type
        adopt_pet_node = self.head
        type = adopt_pet_node.type

        # Removes the adopted pet from the head of the queue of `type`
        self.heads[type] = adopt_pet_node.typeNext

        # Removes the adopted pet from the head of the global queue
        self.head = adopt_pet_node.next
        if self.head:
            self.head.prev = None

        # Case in which the adopted pet was the tail of `type`
        if adopt_pet_node == self.tails[type]:
            self.tails[type] = None
            # Case in which adopted pet is global tail
            if adopt_pet_node == self.tail:
                self.tail = None

        return adopt_pet_node.data

    def dequeueType(self, type):
        assert type in self.types
        adopt_pet_node = self.heads[type]
        if adopt_pet_node == None:
            raise Exception("No {}s are in the shelter".format(type))

        # Case in which adopted pet is global head
        if adopt_pet_node == self.head:
            return self.dequeueAny()
        # Otherwise, adopt_pet_node.prev exists, so we must 'glue' ends together
        else:
            adopt_pet_node.prev.next = adopt_pet_node.next
            if adopt_pet_node.next:
                adopt_pet_node.next.prev = adopt_pet_node.prev

        # Case in which adopted pet is tail of `type`
        if adopt_pet_node == self.tails[type]:
            self.tails[type] = None
            # Case in which adopted pet is global tail
            if adopt_pet_node == self.tail:
                self.tail = self.tail.prev

        self.heads[type] = adopt_pet_node.typeNext

        return adopt_pet_node.data


ash = AnimalShelter()
ash.enqueue("Fred", "dog")
ash.enqueue("Freddy", "cat")
ash.enqueue("Frederick", "dog")
assert ash.dequeueAny() == "Fred"
assert ash.dequeueType("dog") == "Frederick"
assert ash.dequeueType("cat") == "Freddy"
