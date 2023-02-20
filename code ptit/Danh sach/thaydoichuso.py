


def sum_min(a, b, p, q):
    a1 = a.replace(str(q), str(p))
    b1 = b.replace(str(q), str(p))
    return int(a1) + int(b1)

def sum_max(a, b, p, q):
    a1 = a.replace(str(p), str(q))
    b1 = b.replace(str(p), str(q))
    return int(a1) + int(b1)

def solve():
    t = int(input())
    for _ in range(t):
        p, q = map(int, input().split())
        a = input().strip()
        if(a.count(' ')):a, b = a.split()
        else: b = input()
        if p > q:
            tmp = p
            p = q
            q = tmp
        print(sum_min(a, b, p, q), sum_max(a, b, p, q))

def main():
    solve()

if __name__ == "__main__":
    main()