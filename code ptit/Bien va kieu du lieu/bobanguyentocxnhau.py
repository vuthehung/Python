

import math
import itertools

def bo3ngto(a, b, c):
    a_b = int(math.gcd(a, b))
    a_c = int(math.gcd(a, c))
    b_c = int(math.gcd(b, c))
    return a_b == 1 and a_c == 1 and b_c == 1    

def solve():
    l, r = map(int, input().split())
    arr = []
    for i in range(l, r + 1):
        arr.append(i)
    for i in itertools.combinations(arr, 3):
        if bo3ngto(i[0], i[1], i[2]):
            print(i)
def main():
    solve()

if __name__ == "__main__":
    main()