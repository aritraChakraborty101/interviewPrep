# You're given a 2D integer array matrix. Return the transpose of matrix.

def transposeMatrix(matrix):
    result = []
    for i in range(len(matrix[0])):
        result.append([])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[j].append(matrix[i][j])

    return result


print(transposeMatrix([
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]))

print(transposeMatrix([
    [1, 2],
    [3, 4],
    [5, 6]
]))