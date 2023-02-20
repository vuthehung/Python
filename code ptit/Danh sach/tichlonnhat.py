

def solve():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    tmp = []
    print(max(a[0]*a[1], a[-1]*a[-2], a[0]*a[1]*a[-1], a[-1]
        * a[-2]*a[-3], a[0]*a[1]*a[2], a[-1]*a[-2]*a[0]))

def main():
    solve()

if __name__ == "__main__":
    main()  