# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    #need a dummy node 
    # the next element to the head become the new head
    # the head points at the dummmy node 
    # the old head becomes the tail of the dummy node

    firstPointer = None
    secondPointer = head
    while secondPointer:
        thirdPointer = secondPointer.next
        secondPointer.next = firstPointer
        firstPointer = secondPointer
        secondPointer = thirdPointer

    return firstPointer
