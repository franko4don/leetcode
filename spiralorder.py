
def spiral_order(matrix):
    row = len(matrix)
    col = len(matrix[0])
    count = col * row
    track = 0
    m = 0
    n = 0
    new_matrix = []

    while track <= count:
        for i in range(n, col - n):
            new_matrix.append(matrix[m][i])
            track += 1
        # if track >= count:
        #     break

        for i in range(m + 1, row - m):
            new_matrix.append(matrix[i][col - 1 - n])
            track += 1
        # if track >= count:
        #     break

        for i in range(col - n - 2, -1 + n, -1):
            new_matrix.append(matrix[row - 1 - m][i])
            track += 1
        # if track >= count:
        #     break

        for i in range(row - m - 2, 0 + m, -1):
            new_matrix.append(matrix[i][m])
            track += 1
        if track >= count:
            break
        m += 1
        n += 1

    return new_matrix

record = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

record2 = [[1, 2, 3 ,4],
           [5, 6, 7, 8],
           [9,10,11,12],
           [13,14,15,16]
           ]

record3 = [[1, 2, 3, 4,  5],
           [6, 7, 8, 9, 10],
           [11,12,13,14,15],
           [16,17,18,19,20],
           [21,22,23,24,25]]

print(spiral_order(record3))