

import math 

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        res = "1"
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                cnt = 0
                while n % i == 0:
                    n /= i
                    cnt += 1
                res += " * " + str(i) + "^" + str(cnt)
        if n != 1:
            res += " * " + str(int(n)) + "^1"
        print(res)
def main():
    solve()

if __name__ == "__main__":
    main()