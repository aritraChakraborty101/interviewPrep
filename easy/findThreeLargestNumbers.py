#write a function that takes in an array of at least three integers and, without
#sorting the input array returns a sorted array of the largest three digit of the 
#array

def findThreeLargestNumbers(array):
    result = [array[0], array[1], array[2]]
    result.sort()

    if len(array) == 3:
        return result 

    for i in range(3, len(array)):
        
        if array[i] > result[0]:
            result[0] = array[i]
            result.sort()

    result.sort()
    return result
