#given an array and return the first duplicate value with the minimum index

def secondMax(arr):
    arr.sort()
    return arr[1]

def firstDuplicateValue(array):
    val = False
    flag = {}
    result = []
    for i in range(len(array)):
        if array[i] not in flag:
            flag[array[i]] = [i]
        else:
            flag[array[i]].append(i)
    
    for key, value in flag.items():
        if len(value) > 1:
            val = True
            result.append(secondMax(value))
    if not val:
        return -1
    return array[min(result)]
            
