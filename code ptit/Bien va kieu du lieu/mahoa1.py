
def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        cnt = 1
        l = len(s)
        for i in range(0, l - 1):
            if s[i] == s[i + 1]:
                cnt += 1
            else:
                print(cnt, s[i], sep='', end='')
                cnt = 1
        print(cnt, s[l - 1], sep='', end='')                
        print()
def main():
    solve()

if __name__ == "__main__":
    main()