
def thuanNghich(n):
    return n == n[::-1]

def doiCoSo(n, k):
    res = ''
    tmp = n
    while tmp > 0:
        du = tmp % k
        if du >= 10:
            res += str(chr(du + 55))
        else:
            res += str(du)
        tmp = tmp // k
    return ''.join(reversed(res))

a, b, m = map(int, input().split())
res = []
for i in range(a, b + 1):
    tmp = 0
    for j in range(2, m + 1):
        if thuanNghich(doiCoSo(i, j)):
            tmp = i
        else:
            tmp = 0
            break
    if tmp != 0:
        res.append(tmp)
print(len(res))