#You are given a binary expression tree. write a function to evaluate this tree mathematically
# and return a single resulting integer

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def call(first, second, op):
    if op is -1:
        return first + second
    elif op is -2:
        return  first - second
    elif op is -3:
        return int(first / second)
    else:
        return first * second
        
def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value

    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    return call(leftValue, rightValue, tree.value)
