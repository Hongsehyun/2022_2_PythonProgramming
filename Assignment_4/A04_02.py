matrix_A = [
    [1,2],
    [3,4]
]

matrix_B = [
    [5,6],
    [7,8]
]

matrix_C = [
    [None,None],
    [None,None]
]

### YOUR CODE STARTS HERE
for i in range(len(matrix_A)):
    for j in range(len(matrix_A[0])):
        matrix_C[i][j] = matrix_A[i][j]+matrix_B[i][j]
### YOUR CODE ENDS HERE
print(matrix_C)

"""
### YOUR EXPLANATION STARTS HERE
This program performs 'Add' operations for two matrices of the same size and prints out the operational results.

Line by Line Explanation
Line 01 ~ 04 : Defines a 2 by 2 matrix named 'matrix_A' using a double list.
Line 06 ~ 09 : Defines a 2 by 2 matrix named 'matrix_B' using a double list.
Line 11 ~ 14 : Defines a 2 by 2 empty matrix named 'matrix_C' using a double list.

Line 17      : Performs as many iterations as the number of rows.
               Since the index starts at 0, I used 'range' function to access the index.
Line 18      : Performs as many iterations as the number of columns.
               Since the index starts at 0, I used 'range' function to access the column.
Line 19      : Within a repeat statement, I approached the same positions of the two matrices to perform 'Add' operations,
               and then store the operational results in the same position.

Line 21      : Prints out the result of sum of the matrices.
### YOUR EXPLANATION ENDS HERE
"""