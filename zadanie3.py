def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "YES"
    else:
        return "NO"


x1, x2, x3 = map(int, input().split())
print(triangle(x1, x2, x3))
