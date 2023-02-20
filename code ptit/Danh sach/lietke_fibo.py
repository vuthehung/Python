
def solve():
    l = []
    f1 = 1
    f2 = 1
    fb = 0
    l.append(f1)
    l.append(f2)
    for i in range(3, 93):
        fb = f1 + f2
        f1 = f2
        f2 = fb
        l.append(fb)
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        for i in range(a - 1, b):
            print(l[i], end=' ')
        print()
def main():
    solve()

if __name__ == "__main__":
    main()