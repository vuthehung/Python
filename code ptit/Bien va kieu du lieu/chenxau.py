
def solve():
    s1 = input()
    s2 = input()
    p = int(input())
    res = ""
    for i in range(0, p - 1):
        res = res + s1[i]
    for i in range(len(s2)):
        res = res + s2[i]
    for i in range(p - 1, len(s1)):
        res = res + s1[i]
    print(res)
def main():
    solve()

if __name__ == "__main__":
    main()