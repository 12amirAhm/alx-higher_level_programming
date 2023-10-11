#!/usr/bin/python3
s_m_s = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = s_m_s(matrix)
print(new_matrix)
print(matrix)
