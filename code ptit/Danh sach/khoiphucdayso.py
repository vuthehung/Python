
def solve():
    n = int(input())
    a = []
    for _ in range(n):
        a.append([int(j) for j in input().split()])
    res = []
    #tinh so dau tien cua day ban dau
    res.append((a[0][1] + a[0][2] - a[1][2]) // 2)
    for i in range(1, n):
        res.append(a[0][i] - res[0])
    print(*res)

def main():
    solve()

if __name__ == "__main__":
    main()