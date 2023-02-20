def solve():
    t = int(input())
    cnt = 0
    a = []
    d = dict()
    for i in range(t):
        s = input()
        if len(s) != 0:
            a.append(s)
        if len(s) == 0 or i == t - 1:
            d[a[0]] = len(a) - 1
            a.clear()
    for i in d.items():
        print(f"{i[0]}: {i[1]}")

def main():
    solve()

if __name__ == "__main__":
    main()

