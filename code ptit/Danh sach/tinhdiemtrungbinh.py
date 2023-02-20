from collections import Counter

def solve():
    n = int(input())
    arr = list(map(float, input().split()))
    sort = sorted(arr)
    min = sort[0]
    max = sort[n - 1]
    tmp = []
    for i in arr:
        if i > min and i < max:
            tmp.append(i)
    aver = sum(tmp) / len(tmp)
    print(f"{aver:.2f}")
def main():
    solve()

if __name__ == "__main__":
    main()