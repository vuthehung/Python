

def solve():
    t = int(input())
    for _ in range(t):
        l1 = list(input())
        l2 = sorted(l1)
        if l1 == l2:
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()