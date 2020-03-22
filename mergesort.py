def merge_list(a, b):
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    rem = a[i:] if i < len(a) else b[j:]

    return c + rem


a = [9, 3, 7, 5, 6, 6, 4, 8, 2, 18]
b = [[i] for i in a]

for i in range(len(b) - 1):
    res = merge_list(b[i], b[i + 1])
    b[i + 1] = res

print(b[len(b) - 1])
