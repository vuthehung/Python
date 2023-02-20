def xuLy(n):
    res = ""
    for i in n:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            res += " "
        else:
            res += i
    return res
def solve():
    n = int(input())
    l = []
    for _ in range(n):
        s = input()
        tmp = list(map(int, xuLy(s).split()))
        l.extend(tmp)
    sort = sorted(l)
    for i in sort:
        print(i)
def main():
    solve()

if __name__ == "__main__":
    main()