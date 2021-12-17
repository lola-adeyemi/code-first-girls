"""
SEARCH IN MATRIX
--------
You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.
Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].
EXAMPLE INPUT

"""

matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]


# target =44
# EXAMPLE OUTPUT
# result = [3,3]


def search_in_matrix(matrix, target):
    a_max = len(matrix)  # find the number of rows
    check = 0

    for a in range(0, a_max, 1):  # range through row numbers
        b_max = len(matrix[a])  # calculate number of columns
        for b in range(0, b_max, 1):  # range through columns for the row number
            result = [a, b]
            check = matrix[a][b]  # get item to check from matrix
            if check == target:
                return print(result)

    if check != target:
        result = [-1, -1]
        print(result)


search_in_matrix(matrix, 1060)
