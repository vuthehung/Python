def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = dict()
    for i in a:
        d[i] = a.count(i)
    d = dict(sorted(d.items(), key= lambda el : (n - el[1], el[0])))
    check = 0
    value = list(d.values())
    max = value[0]
    for i in d.items():
        if max > i[1]:
            check = 1
            print(i[0])
            break
    if check == 0:
        print("NONE")
    

def main():
    solve()

if __name__ == "__main__":
    main()