
def solve():
    n = int(input())
    l = []
    test = n
    while test>0: 
        data = input() 
        base =  list(map(int, data.split()))
        l.extend(base)
        test -= len(base)
    for i in range(n - 1):
        if l[i] % 2 == 0:
            for j in range(i + 1, n):
                if l[i] > l[j] and l[j] % 2 == 0:
                    tmp1 = l[i]
                    l[i] = l[j]
                    l[j] = tmp1
        else:
            for k in range(i + 1, n):
                if l[i] < l[k] and l[k] % 2 != 0:
                    tmp2 = l[i]
                    l[i] = l[k]
                    l[k] = tmp2
    print(*l)

def main():
    solve()

if __name__ == "__main__":
    main()