
def solve():
    while True:
        a = list(map(int, input().split()))
        if a[0] == a[1] == a[2] == a[3] == 0:
            break
        cnt = 0
        while not(a[0] == a[1] == a[2] == a[3]):
            tmp = a[0]
            for i in range(3):
                a[i] = abs(a[i] - a[i + 1])
            a[3] = abs(tmp - a[3])
            cnt += 1
            if a[0] == a[1] == a[2] == a[3]:
                break
        print(cnt)

    

def main():
    solve()

if __name__ == "__main__":
    main()