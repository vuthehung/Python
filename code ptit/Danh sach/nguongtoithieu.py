from collections import Counter
def solve():
    s = input()
    k = int(input())
    l = []
    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            l.append(s[i : i + 2])
    else:
        for i in range(0, len(s) - 1, 2):
            l.append(s[i : i + 2])
    l_s = sorted(l)
    cnt = Counter(l_s)
    check = 0
    for i in cnt:
        if cnt[i] >= k:
            check = 1
            print(i, cnt[i])
    if check == 0:
        print("NOT FOUND")
def main():
    solve()

if __name__ == "__main__":
    main()