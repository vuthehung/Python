
t = int(input())
for _ in range(t):
    s = input()
    tmp = ""
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            tmp += " "
        else:
            tmp += s[i]
    l = list(map(int, tmp.split()))
    print(min(l))
