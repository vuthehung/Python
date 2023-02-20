def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        if s[len(s) - 1] == '6' and s[len(s) - 2] == '8':
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()