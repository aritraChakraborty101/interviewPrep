def binarySearch(array, target):
    if len(array) == 1:
        if array[0] == target:
            return 0
        else:
            return -1
    start = 0
    end = len(array) - 1
    mid = (start + end)// 2

    while start <= end:
        mid = (start + end)// 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1
            
