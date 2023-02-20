
def solve():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append([int(j) for j in input().split()])

    if n > m:
        tmp = n - m
        i = 1
        while tmp > 0:
            tmp -= 1
            del a[i - 1]
            i += 1
    else:
        tmp = m - n
        i = 2
        while tmp > 0:
            tmp -= 1
            for j in range(n):
                del a[j][i - 1]
            i += 1
    for i in a:
        print(*i)

def main():
    solve()

if __name__ == "__main__":
    main()


