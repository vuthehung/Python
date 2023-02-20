
def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        tmp = ""
        for i in range(len(s)):
            
            if s[i] >= 'a' and s[i] <= 'z':
                tmp += " "
            else:
                tmp += s[i]
        l = list(map(int, tmp.split()))
        l_sort = sorted(l)
        print(l_sort[0])
def main():
    solve()

if __name__ == "__main__":
    main()