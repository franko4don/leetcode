def generate(numRows):
    answer = []
    for i in range(numRows):
        if len(answer) == 0:
            answer.append([1])
        else:
            value = answer[i - 1]
            temp = []
            for j in range(len(value) - 1):
                temp.append(value[j] + value[j + 1])
            temp = [1] + temp + [1]

            answer.append(temp)
    return answer


print(generate(15))