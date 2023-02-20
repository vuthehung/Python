def sum(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum % 10 == 0
def conditon2(s):
    for i in range(len(s) - 1):
        if(abs(int(s[i]) - int(s[i + 1])) != 2):
            return False
            break
    return True
def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        if sum(n) and conditon2(n):
            print("YES")
        else:
            print("NO")


def main():
    solve()

if __name__ == "__main__":
    main()
