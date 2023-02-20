n = int(input())
d = {}
check = 1

for _ in range(n - 1):
    x, y = [int(i) for i in input().split()]
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
    if y in d:
        d[y] += 1
    else:
        d[y] = 1

for i in range(1, n + 1):
    if (i not in d) or (d[i] != 1 and d[i] != n - 1):
        check = 0
        print('No')
        break
if check:
    print('Yes')