# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    slowNode = linkedList
    fastNode = linkedList
    while fastNode.next and fastNode.next.next:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
    if fastNode.next:
        return slowNode.next
    else:
        return slowNode
