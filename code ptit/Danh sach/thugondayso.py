def solve():
    
    n = int(input())
    l = list(map(int, input().split()))
    res = []
    for i in l:
        if len(res) and i % 2 == res[-1] % 2:
            res.pop()
        else:
            res.append(i)
    print(len(res))
def main():
    solve()

if __name__ == "__main__":
    main()