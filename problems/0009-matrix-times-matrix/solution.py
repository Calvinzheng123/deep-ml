def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    if not a or not b or len(a[0]) != len(b):
        return -1
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
