
def solve():
    t = int(input())
    for _ in range(t):
        n =  input()
        if int(n) < 10:
            print(n)
        else:
            tmp = 0
            flag = 0
            res = ""
            for i in range(len(n) - 1, 0, -1):
                tmp = ord(n[i]) - 48 + flag
                if tmp >= 5:
                    flag = 1
                else:
                    flag = 0
                res = '0' + res
            tmp = ord(n[0]) - 48 + flag
            res = str(tmp) + res
            print(res)
def main():
    solve()

if __name__ == "__main__":
    main()