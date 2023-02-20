def check(n):
    for i in n:
        if i != '0' and i != '1' and i != '2':
            return False
            break
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()