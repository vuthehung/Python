def Solve():
    n, m, L = map(int, input().split())
    a = [[int(x) for x in input().split()] for i in range(n)]
    prefix_sum_row = [[0 for j in range(m+1)] for i in range(n+1)]
    for j in range(1, m+1):
        for i in range(1, n+1):
            prefix_sum_row[i][j] = prefix_sum_row[i-1][j]+a[i-1][j-1]
    dp = [[0 for j in range(m+1)] for i in range(n-L+2)]
    for i in range(1, n-L+2):
        for j in range(1, m+1):
            dp[i][j] = dp[i][j-1]+prefix_sum_row[i+L-1][j]-prefix_sum_row[i-1][j]
    for i in range(1, n-L+2):
        for j in range(L, m+1):
            print((dp[i][j]-dp[i][j-L])//(L*L), end=" ")
        print()


for _ in range(int(input())):
    Solve()