
def solve():
    t = int(input())
    d = dict()
    for _ in range(t):
        id_sub = input()
        a = []
        a.append(input())
        a.append(input())
        d[id_sub] = a
    d = dict(sorted(d.items(), key= lambda el : el[0]))
    for i in d.items():
        print(f"{i[0]} {i[1][0]} {i[1][1]}")

def main():
    solve()

if __name__ == "__main__":
    main()

