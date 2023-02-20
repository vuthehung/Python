
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
        if sum_cs % 3 == 0:
            print("YES")
        else:
            print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()