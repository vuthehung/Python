t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = []
    kernel = []
    res = 0
    for i in range(n):
        x.append(list(map(int, input().split())))
    for i in range(3):
        kernel.append(list(map(int, input().split())))

    for i in range(2, n):
        for j in range(2, m):
            res += kernel[0][0] * x[i - 2][j - 2]
            res += kernel[0][1] * x[i - 2][j - 1]
            res += kernel[0][2] * x[i - 2][j]
            res += kernel[1][0] * x[i - 1][j - 2]
            res += kernel[1][1] * x[i - 1][j - 1]
            res += kernel[1][2] * x[i - 1][j]
            res += kernel[2][0] * x[i][j - 2] 
            res += kernel[2][1] * x[i][j - 1]
            res += kernel[2][2] * x[i][j]
    print(res)

