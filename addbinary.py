def add_binary(a, b):
    result = bin(int(a, 2) + int(b, 2))
    return result[2:]

def strStr(haystack, needle):
    answer = -1
    if haystack == needle:
        return 0
    for i in range(0, len(haystack)):
        print(haystack[i:len(needle) + i])
        if haystack[i:len(needle) + i] == needle:
            answer = i
            break
    return answer

def longestCommonPrefix(strs):
    answer = ""
    shortest = "*" * 2000
    if len(strs) == 0:
        return ""
    for i in range(len(strs)):
        if len(strs[i]) < len(shortest):
            shortest = strs[i]

    if len(shortest) == 0:
        return ""

    for i in range(0, len(shortest)):
        needle = shortest[0:i + 1]
        count = 0
        for j in range(len(strs)):
            if needle == strs[j][0:i + 1]:
                count += 1
        if count == len(strs):
            if len(needle) > len(answer):
                answer = needle

    return answer

l = "hello"
print(longestCommonPrefix(['a']))