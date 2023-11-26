# You're given a 2D integer array matrix. Return the transpose of matrix.

def transposeMatrix(matrix):
    result = []
    for i in range(len(matrix[0])):
        result.append([])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[j].append(matrix[i][j])

    return result
