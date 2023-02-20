

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        max1 = max(arr)
        arr.remove(max1)
        max2 = max(arr)
        arr.remove(max2)
        max3 = max(arr)
        print(max1 + max2 + max3)

def main():
    solve()

if __name__ == "__main__":
    main()