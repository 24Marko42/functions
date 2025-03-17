def matrix(n=None, m=None, a=0):
    if n == None and m == None:
        n = 1
        m = 1
    elif m == None:
        m = n
    return [[a for i in range(m)] for j in range(n)]


rows = matrix()
for row in rows:
    print(*row)
print()
rows = matrix(2)
for row in rows:
    print(*row)
