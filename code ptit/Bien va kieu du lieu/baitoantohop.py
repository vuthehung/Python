
import itertools

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    for i in itertools.combinations(res, k):
        print(*i)
           

def main():
    solve()

if __name__ == "__main__":
    main()