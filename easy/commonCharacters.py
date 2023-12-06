#write a function that takes in a non-empty string and return a list of characters that 
#are common to all strings in the list, ignoring multiplicity

def commonCharacters(strings):
    temp = {}
    result = []
    start = strings[0]

    for i in start:
        temp[i] = 1

    for i in range(1, len(strings)):
        for j in strings[i]:
            if j in temp.keys() and temp[j] == i:
                temp[j] += 1

    for key in temp.keys():
        if temp[key] == len(strings):
            result.append(key)

    return result
            
