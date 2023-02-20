import itertools

def solve():
    n, k = map(int, input().split())
    s = set(input().split())
    a = list(s)
    a_s = sorted(a)
    for i in itertools.combinations(a_s, k):
        print(*i)

def main():
    solve()

if __name__ == "__main__":
    main()