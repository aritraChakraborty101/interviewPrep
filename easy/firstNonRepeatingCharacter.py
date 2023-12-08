# write a function that return the first non repeating number's index from a string
# if there is none return -1 

def firstNonRepeatingCharacter(string):
    result = {}
    flag = False
    min = float('inf')
    for i in range(len(string)):
        if string[i] not in result:
            result[string[i]] = i
        else:
            result[string[i]] = False
    for key in result.keys():
            if result[key] is not False and result[key] < min:
                min = result[key]
                flag = True
    if flag:
        return min
    else:
        return -1
            
