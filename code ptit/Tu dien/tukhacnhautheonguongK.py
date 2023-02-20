
def solve():
    t, k = map(int, input().split())
    text = ''
    for _ in range(t):
        s = input().lower()
        text = text + " " + s
    tmp = ''
    for i in text:
        if not(i.isalpha()) and not(i.isnumeric()):
            tmp += ' '
        else:
            tmp += i
    a = list(tmp.split())
    d = dict()
    for i in a:
        if a.count(i) >= k:
            d[i] = a.count(i)
    d = dict(sorted(d.items(), key= lambda el : (500 - el[1], el[0])))
    for i in d.items():
        print(f"{i[0]} {i[1]}")
        
def main():
    solve()

if __name__ == "__main__":
    main()