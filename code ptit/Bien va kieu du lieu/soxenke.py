
def condi1(n):
    return len(n) % 2 != 0

def condi2(n):
    return n[0] != n[1]

def condi3(n):
    for i in range(2, len(n) + 1, 2):
        if n[0] != n[i]:
            return False
            break
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        if condi1(n) and condi2(n) and condi2(n):
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()