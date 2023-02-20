from itertools import permutations

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = []
        for i in range(n, 0, -1):
            l.append(str(i))
        cnt = 0
        res = []
        for i in permutations(l, n):
            cnt += 1
            res.append(''.join(i))
        print(cnt)
        print(*res)

def main():
    solve()

if __name__ == "__main__":
    main()