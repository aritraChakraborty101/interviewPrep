#Write a function that takes a Binary tree and return the sum of it's nodes depth

def nodeDepths(root):
    def findRight(root, temp = 0):
        if not root:
            return 0
        return temp + findRight(root.left, temp + 1) + findRight(root.right, temp + 1)
        
    return findRight(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
