
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        stack = []
        res = []
        for i in range(n):
            while len(stack) > 0 and a[stack[-1]] <= a[i]:
                stack.pop()
            if len(stack) > 0:
                res.append(i - stack[-1])
            else:
                res.append(i + 1)
            stack.append(i)
        print(*res)

def main():
    solve()

if __name__ == "__main__":
    main()