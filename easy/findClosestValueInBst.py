def findClosestValueInBst(tree, target):
    def findClosest(tree, closest):
        if not tree:
            return closest

        if abs(target - tree.value) < abs(target - closest):
            closest = tree.value

        if target < tree.value:
            return findClosest(tree.left, closest)

        elif target > tree.value:
            return findClosest(tree.right, closest) 

        return closest

    return findClosest(tree, float('inf'))
