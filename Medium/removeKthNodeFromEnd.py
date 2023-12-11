# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def countNode(head):
    temp = head
    len = 0
    while temp:
        temp = temp.next
        len += 1
    return len

def removeKthNodeFromEnd(head, k):
    len = countNode(head)
    removePosition = len - k + 1

    if removePosition == 1:
        nextNode = head.next
        head.value = head.next.value 
        head.next = head.next.next
        nextNode.next = None
        return 
    temp = head
    prev = None

    for i in range(removePosition - 1):
        prev = temp
        temp = temp.next

    prev.next = temp.next
    temp.next = None
