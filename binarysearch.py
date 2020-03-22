def search(data, needle):
    exists = -1
    length = len(data) // 2
    if length == 0:
        exists = data[0] == needle
        print(exists)
        return exists
    if needle >= data[length]:
        search(data[length:], needle)
    else:
        search(data[0:length], needle)
    return exists


def binary_search(nums, target):
    l = 0
    h = len(nums)
    m = 0
    while l < h - 1:
        m = (l + h) // 2
        if target > nums[m]:
            l = m
        else:
            h = m
    if nums[l] == target:
        return l
    elif h < len(nums) and nums[h] == target:
        return h
    else:
        return -1



a = [4,5,6,7,0,1,2]
result = binary_search(a, 0)

print(result)
