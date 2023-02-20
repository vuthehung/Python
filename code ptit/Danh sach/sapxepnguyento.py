 
import math

def prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
            break
    return True

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        if prime(arr[i]):
            for j in range(i + 1, n):
                if prime(arr[j]):
                    if arr[i] > arr[j]:
                        tmp = arr[i]
                        arr[i] = arr[j]
                        arr[j] = tmp
    print(*arr)
    
def main():
    solve()

if __name__ == "__main__":
    main()