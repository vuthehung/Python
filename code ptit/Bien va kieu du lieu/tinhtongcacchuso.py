
def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        sum = 0
        l = []
        for i in s:
            if i >= '0' and i <= '9':
                sum += int(i)
            else:
                l.append(i)
        l_sort = sorted(l)
        res = ""
        for i in l_sort:
            res += i
        print(res + str(sum))
def main():
    solve()

if __name__ == "__main__":
    main()