def Try(s, n, a, b, c):
    if len(s) == n and a <= b and b <= c and a > 0:
        print(s)
    if len(s) < n:
        Try(s + 'A', n, a + 1, b, c)
        Try(s + 'B', n, a, b + 1, c)
        Try(s + 'C', n, a, b, c + 1)

def solve():
    n = int(input())
    for i in range(3, n + 1):
        Try('', i, 0, 0, 0)

def main():
    solve()

if __name__ == "__main__":
    main()