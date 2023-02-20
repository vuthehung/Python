import math

def solve():
    n = int(input())
    row = [0] * n; col = [0] * n
    for i in range(n):
        txt = input()
        for j in range(len(txt)):
            if txt[j] == 'C':
                row[i] += 1
                col[j] += 1
    res = 0
    for i in row:
        if i >= 2:
            res += math.comb(i, 2)
    for i in col:
        if i >= 2:
            res += math.comb(i, 2)
    print(res)



def main():
    solve()

if __name__ == "__main__":
    main()