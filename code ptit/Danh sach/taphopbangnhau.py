
def solve():
    n, m = map(int, input().split())
    a = [int(j) for j in input().split()]
    b = [int(j) for j in input().split()]
    a.sort()
    b.sort()
    a_a = []; b_a = []
    for i in a:
        if i not in a_a:
            a_a.append(i)
    for i in b:
        if i not in b_a:
            b_a.append(i)
    if a_a == b_a:
        print("YES")
    else:
        print("NO")
def main():
    solve()

if __name__ == "__main__":
    main()