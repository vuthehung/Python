
def solve():
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split())
        a = list(map(int, input().split()))
        a1_sub = a[0 : d]
        a2_sub = a[d : len(a)]
        res = []
        res.extend(a2_sub)
        res.extend(a1_sub)
        print(*res)
    

def main():
    solve()

if __name__ == "__main__":
    main()