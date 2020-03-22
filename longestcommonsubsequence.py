import numpy as np

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# temp = [[0] * (m + 1)] * (n + 1)
temp = [[0 for i in range(m+1)] for j in range(n+1)]

value = 8755

for i in range(1, n + 1):

    for j in range(1, m + 1):

        if a[i - 1] == b[j - 1]:
            temp[i][j] = temp[i - 1][j - 1] + 1
        else:
            temp[i][j] = max(temp[i-1][j], temp[i][j - 1])

# print(np.matrix(temp))
answer = ''
i = n
j = m
while i != 0 and j != 0:

    if temp[i - 1][j] == temp[i][j]:
        i -= 1
        continue
    if temp[i][j - 1] == temp[i][j]:
        j -= 1
        continue

    if temp[i - 1][j - 1] < temp[i][j]:
        i -= 1
        j -= 1
        value = a[i]
        # print(value)
        answer = str(value) + ' ' + answer
        continue

print(answer)



