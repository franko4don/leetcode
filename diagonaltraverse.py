
def diagonal_traverse(matrix):
    left = []
    right = []
    end_row = len(matrix)
    last = False
    end_column = len(matrix[0]) if end_row > 0 else 0
    sub = []
    for i in range(end_row):
        row = i
        col = 0
        sub.clear()
        while row >= 0 and col < end_column:
            if i % 2 != 0:
                last = True
                sub.insert(0, matrix[row][col])
            else:
                left.append(matrix[row][col])
                last = False
            row -= 1
            col += 1
        left.extend(sub)

    for j in range(1, end_column):
        row = end_row - 1
        col = j
        sub.clear()
        while row >= 0 and col < end_column:
            if last == False:
                sub.insert(0, matrix[row][col])

            else:
                right.append(matrix[row][col])

            row -= 1
            col += 1

        right.extend(sub)
        last = not last

    left.extend(right)
    return left

record = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

record2 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

record3 = [[2,5,8],
           [4,0,-1]]

record4 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]

print(diagonal_traverse(record3))