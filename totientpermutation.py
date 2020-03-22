def compute(N):
    factors = {}
    N = N + 1
    a = [0] * N
    for m in range(N):
        factors[m] = []
    print(factors);
    for i in range(1, N):

        for j in range(i, N, i):
            print (j)
            factors[j].append(j)
            # print (factors[j].append(j))

            a[j] += 1
    #     print(factors)
    print(factors)

compute(100)