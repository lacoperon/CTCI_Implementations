'''
Elliot Williams
08/02/18

Q: `Rotate Matrix`: Given an image represented by an NxN matrix, where each
   pixel in the image is 4 bytes, write a method to rotate the image by 90
   degrees. Can you do this in place?
'''
import math

def rotateMatrix(matrix):
    N = len(matrix)

    # Switches the TL
    for i in range(math.ceil(N/2)):
        for j in range(math.ceil(N/2)):
            temp1 = matrix[i][j]
            temp2 = matrix[j][N-i-1]
            temp3 = matrix[N-i-1][N-j-1]
            matrix[i][j] = matrix[N-j-1][i]
            matrix[j][N-i-1] = temp1
            matrix[N-i-1][N-j-1] = temp2
            matrix[N-j-1][i] = temp3
    return matrix

# Time  Complexity: O(N^2)
# Space Complexity: O(1)

matrix_one = [["a","b"], ["c","d"]]
matrix_two = [["a","b","c","d"],
              ["e","f","g","h"],
              ["i","j","k","l"],
              ["m","n","o","p"]]


assert rotateMatrix(matrix_one) == [["c","a"], ["d","b"]]
assert rotateMatrix(matrix_two) == [["m","i","e","a"],
                                    ["n","j","f","b"],
                                    ["o","k","g","c"],
                                    ["p","l","h","d"]]
