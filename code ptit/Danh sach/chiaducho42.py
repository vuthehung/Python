def solve():
    l = []
    test = 10 
    while test>0: 
        data = input() 
        base =  list(map(int, data.split()))
        l.extend(base)
        test -= len(base)
    s = set()
    for i in l:
        s.add(i % 42)
    print(len(s))
def main():
    solve()

if __name__ == "__main__":
    main()