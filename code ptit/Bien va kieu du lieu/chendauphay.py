def solve():
    n = input()
    i = len(n) - 1
    cnt = 0
    res = ""
    while 1:
        cnt += 1
        res = n[i] + res
        if i == 0:
            break
        if cnt == 3:
            res = ',' + res
            cnt = 0
        i -= 1
    print(res)
def main():
    solve()

if __name__ == "__main__":
    main()