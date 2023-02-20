
def solve():
    n, m = map(int, input().split())
    a = [int(j) for j in input().split()]
    b = [int(j) for j in input().split()]
    a.sort()
    b.sort()
    res1 = []; res2 = []; res3 = []
    a_a = []; b_a = []
    for i in a:
        if i not in a_a:
            a_a.append(i)
    for i in b:
        if i not in b_a:
            b_a.append(i)
    for i in a_a:
        if i in b_a:
            res1.append(i)
    for i in a_a:
        if i not in b_a:
            res2.append(i)
    for i in b_a:
        if i not in a_a:
            res3.append(i)
    print(*res1)
    print(*res2)
    print(*res3)
def main():
    solve()

if __name__ == "__main__":
    main()