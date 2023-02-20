def solve():
    n = input()
    if n[0] == n[len(n) - 2] and n[1] == n[len(n) - 1]:
        print("YES")
    else:
        print("NO")

def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()