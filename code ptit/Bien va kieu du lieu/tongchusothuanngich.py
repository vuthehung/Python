
def thuanghich(n):
    res = n[::-1]
    if len(n) <= 1:
        return False
    return res == n

def tongcs(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        sum_cs = tongcs(n)
        if thuanghich(str(sum_cs)):
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()