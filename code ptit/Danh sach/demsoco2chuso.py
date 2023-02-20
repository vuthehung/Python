from collections import Counter
def solve():
    s = input()
    arr = []
    if len(s) % 2 == 0:
        for i in range(0, len(s) - 1, 2):
            res = ""
            res = s[i] + s[i + 1]
            arr.append(int(res))
    else:
        for i in range(0, len(s) - 2, 2):
            res = ""
            res = s[i] + s[i + 1]
            arr.append(int(res))
    cnt = Counter(arr)
    for i in cnt:
        print(f"{i} {cnt[i]}")

def main():
    solve()

if __name__ == "__main__":
    main()