'''
Elliot Williams
08/02/18

Q: `Zero Matrix`: Write an algorithm such that if an element in an MxN matrix is
   0, its entire row and column are set to 0.
'''
from operator import mul
from functools import reduce

def zeroMatrix(matrix):

    M = len(matrix)
    assert M > 0
    N = len(matrix[0])
    assert N > 0

    rowZero = []
    colZero = []

    # Gets rows to be zeroed
    for row in range(M):
        isZeroed = reduce(mul,matrix[row], 1) == 0
        if isZeroed:
            rowZero.append(row)

    # Gets cols to be zeroed
    for col in range(N):
        isZeroed = reduce(mul, [matrix[i][col] for i in range(M)], 1) == 0
        if isZeroed:
            colZero.append(col)

    # Zeroes appropriate rows
    for row in rowZero:
        for j in range(N):
            matrix[row][j] = 0
    # ... and columns
    for col in colZero:
        for i in range(M):
            matrix[i][col] = 0

    return matrix

# Time  Complexity: O(N^2)
# Space Complexity: O(N)

assert zeroMatrix([[1,1,1],[1,1,1],[1,1,1]]) == [[1,1,1],[1,1,1],[1,1,1]]
assert zeroMatrix([[0,0,1],[0,1,0],[0,0,1]]) == [[0,0,0],[0,0,0],[0,0,0]]
assert zeroMatrix([[0,0,1],[0,1,1],[1,1,1]]) == [[0,0,0],[0,0,0],[0,0,1]]


# Note: You can reduce the space to O(1) by using the first null column,
# row as a 'sentinel' to storing values instead of making a new array

# TODO: Implement this
