
def check(s):
    rev_s = s[::-1]
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(rev_s[i]) - ord(rev_s[i + 1])):
            return False
            break
    return True

def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
def main():
    solve()

if __name__ == "__main__":
    main()