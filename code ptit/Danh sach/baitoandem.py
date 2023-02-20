
def solve():
    n = int(input())
    l = []
    while n > 0: 
        data = input() 
        base =  list(map(int, data.split()))
        l.extend(base)
        n -= len(base)
    l_s = sorted(l)
    mx = l_s[len(l) - 1]
    ok = 0
    for i in range(1, mx + 1):
        if l_s.count(i) == 0:
            ok = 1
            print(i)
    if ok == 0:
        print("Excellent!")

def main():
    solve()

if __name__ == "__main__":
    main()