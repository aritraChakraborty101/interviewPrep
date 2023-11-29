class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    curr = linkedList
    while curr is not None:
        nextNode = curr.next
        while nextNode is not None and nextNode.value == curr.value:
            nextNode = nextNode.next
        curr.next = nextNode
        curr = nextNode
    return linkedList
