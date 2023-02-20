from collections import Counter

def solve():
    t = int(input())
    for i in range(1, t + 1):
        s1 = list(input())
        s2 = list(input())
        cnt1 = Counter(s1)
        cnt2 = Counter(s2)
        if cnt1 == cnt2:
            print(f"Test {i}: YES")
        else:
            print(f"Test {i}: NO")


def main():
    solve()

if __name__ == "__main__":
    main()