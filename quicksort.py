data = [10, 5, 8, 12, 56, 23, 354, 455,54, 15, 6, 3, 5435345433]


def partition(l, h):
    i = l
    j = h
    pivot = data[l]
    while i < j:
        while data[i] <= pivot:
            i += 1

        while data[j] > pivot:
            j -= 1

        if i < j:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

        print(data, i, j)
    temp = data[j]
    data[j] = data[l]
    data[l] = temp
    return j


def quick_sort(l, h):
    if l < h:
        j = partition(l, h)
        quick_sort(l, j)
        quick_sort(j+1, h)

quick_sort(0, len(data) - 1)

print(data)



