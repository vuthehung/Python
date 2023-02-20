
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    tmp = n
    cnt = 0
    i = 0
    while i < n - 1:
        mx = max(a[i], a[i + 1])
        mn = min(a[i], a[i + 1])
        if mx > 2 * mn:
            cnt += 1
            n += 1
            if(mx % 2 == 0):
                a.insert(i + 1, mx // 2)
            else:
                a.insert(i + 1, mx // 2 + 1)
            i -= 1
        i += 1
    print(n - tmp)