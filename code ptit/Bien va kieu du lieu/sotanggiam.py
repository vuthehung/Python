
def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        incre = 0
        decre = 1
        for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                incre = 1
                for j in range(i, len(n) - 1):
                    if n[j] <= n[j + 1]:
                        decre = 0
                        break
                break
            if n[i] == n[i + 1]: decre = 0
        if incre and decre:
            print("YES")
        else:
            print("NO")
def main():
    solve()

if __name__ == "__main__":
    main()