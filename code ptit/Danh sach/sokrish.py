
def giaithua(n):
    gt = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        gt *= i
    return gt

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        sum_gt = 0
        for i in n:
            sum_gt += giaithua(int(i))
        if sum_gt == int(n):
            print("Yes")
        else:
            print("No")

def main():
    solve()

if __name__ == "__main__":
    main()