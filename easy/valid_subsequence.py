# given two non empty array if integers
# write a function that determines whether
# the second array is a subsequence of the first one




def isValidSubsequence1(array, sequence):
    result = []
    start = 0
    for i in sequence:
        for j in range(start, len(array)):
            if i == array[j]:
                start = j + 1
                result.append(array[j])
                break
            else:
                pass
    print(result)
    if len(result) == len(sequence):
        return 'true'
    else:
        return 'false'


def isValidSubsequence2(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if sequence[seqIdx] == array[arrIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)






# test cases

# test 1
# expected: True
print(isValidSubsequence1([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
