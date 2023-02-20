
def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        res = ""
        for i in range(len(s)):
            if s[i] >= '1' and s[i] <= '9':
                for _ in range(int(s[i])):
                    res += s[i - 1]
        print(res)

def main():
    solve()

if __name__ == "__main__":
    main()