def transpose(matrix):
    res = []
    n = len(matrix)
    m = len(matrix[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp+[matrix[i][j]]
        res = res+[tmp]
    return res


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)

matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)
