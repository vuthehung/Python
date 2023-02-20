prime = []

def sang():
    for i in range(1000001):
        prime.append(1)
    prime[0] = 0
    prime[1] = 0
    for i in range(2, 1001):
        if prime[i] == 1:
            for j in range(i * i, 1000001, i):
                prime[j] = 0


def solve():
    sang()
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 0
        for i in range(5, n + 1):
            if prime[i] == 1:
                if prime[i + 2] == 1 and prime[i + 6] == 1 and i + 2 <= n and i + 6 <= n:
                    cnt += 1
                if prime[i + 4] == 1 and prime[i + 6] == 1 and i + 4 <= n and i + 6 <= n:
                    cnt += 1
        print(cnt)
        
        
def main():
    solve()
if __name__ == "__main__":
    main()