
from posixpath import split


def solve():
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while 1:
        nhap = [str(i) for i in input().split()]
        k = int(nhap[0])
        if k == 0: break
        s = nhap[1]
        res = ""
        for i in s:
            idx = P.find(i)
            res += P[(idx + k) % 28]
        print(res[::-1])

        
def main():
    solve()

if __name__ == "__main__":
    main()