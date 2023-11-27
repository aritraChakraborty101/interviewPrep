#Write a function in a binary tree that returns it's branch sums ordered from 
#leftmost branch sum to rightmost branch sum
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calcSum(root, temp, result):
    if not root:
        return result

    temp += root.value

    if not root.left and not root.right:
        result.append(temp)

    calcSum(root.left, temp, result)
    calcSum(root.right, temp, result)
    return result

def branchSums(root):
    return calcSum(root, 0, [])

