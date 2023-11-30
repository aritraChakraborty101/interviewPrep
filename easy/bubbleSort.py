def bubbleSort(array):
    n = len(array)
    if n == 1:
        return array

    for i in range(n):
        for j in range(i, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array
