

def solve():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        i = 0 
        j = 0 
        l = 0
        res = []
        while i < n and j < m and l < k:
            if a[i] == b[j] and b[j] == c[l]:
                res.append(a[i])
                i += 1
                j += 1
                l += 1
            elif a[i] <= b[j] and b[j] <= c[l]:
                i += 1
            elif b[j] <= a[i] and b[j] <= c[l]:
                j += 1
            else:
                l += 1
        if len(res) == 0:
            print("NO")
        else:
            print(*res)

def main():
    solve()

if __name__ == "__main__":
    main()