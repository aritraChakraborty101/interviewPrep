# write a function that takes in a list of numbers
# and a target number and returns two distinct numbers
# in the list that add up to the target number. If no such
# numbers exist, it should return None.
# If there are multiple pairs that add up to the target number,
# return the first pair that adds up to the target number.


# O(n^2) time | O(1) space

# explanation:
# the brute force approach to this problem would be to loop through
# the list of numbers and for each number loop through the list again
# to see if any two numbers add up to the target sum. This would take

def twoNumberSum1(array, targetSum):
    # Write your code here.
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


# O(n) time | O(n) space

# explanation:
# we can use a hash table to solve the problem in linear time.
# the idea is to store each number in a hash table. As soon as we
# encounter a number, we check if the number's complement already
# exists in the hash table. If it does, we have found a solution
# and return immediately. Otherwise, we store the number in the hash
# table and continue iterating.


def twoNumberSum2(array, targetSum):
    # Write your code here.
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


# test cases

# test 1
# expected: [4, 6]
print(twoNumberSum1([4, 6], 10))
print(twoNumberSum2([4, 6], 10))

