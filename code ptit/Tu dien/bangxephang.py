

def solve():
    d = dict()
    t = int(input())
    for _ in range(t):
        name = input()
        work = list(map(int, input().split()))
        d[name] = work    
    d_s1 = dict(sorted(d.items(), key= lambda el : (500 - el[1][0], el[1][1], el[0])))
   
    for i in d_s1.items():
        print(f"{i[0]} {i[1][0]} {i[1][1]}")

def main():
    solve()

if __name__ == "__main__":
    main()