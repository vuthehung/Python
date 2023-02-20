
def solve():
    n = int(input())
    l = list(map(int, input().split()))
    l_s = sorted(l)
    mx = l_s[len(l) - 1]
    ok = 0
    for i in range(1, mx + 1):
        if l_s.count(i) == 0:
            ok = 1
            print(i)
            break
    if ok == 0:
        print(mx + 1)

def main():
    solve()

if __name__ == "__main__":
    main()