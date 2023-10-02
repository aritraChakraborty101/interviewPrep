# write a function that takes in a non-empty array of integers that are sorted
# in ascending order and returns a new array of the same length with the squares
# of the original integers also sorted in ascending order.


def mergeSrotedArrays(arr1, arr2):
    mergedArray = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i]**2 < arr2[j]**2:
            mergedArray.append(arr1[i]**2)
            i += 1
        else:
            mergedArray.append(arr2[j]**2)
            j += 1
    while i < len(arr1):
        mergedArray.append(arr1[i]**2)
        i += 1
    while j < len(arr2):
        mergedArray.append(arr2[j]**2)
        j += 1
    return mergedArray


def sortedSquaredArray(array):
    negative_arr = []
    positive_arr = []

    for i in array:
        if i < 0:
            negative_arr.insert(0, i)
        else:
            positive_arr.append(i)

    return mergeSrotedArrays(negative_arr, positive_arr)




def sortedSquaredArray2(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1
    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]
        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue ** 2
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue ** 2
            largerValueIdx -= 1
    return sortedSquares



# test cases

# test 1
# expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(sortedSquaredArray2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))