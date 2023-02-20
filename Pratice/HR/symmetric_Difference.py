def main():
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    L = list()
    L.extend(a.difference(b))
    L.extend(b.difference(a))
    L.sort()
    for i in L:
        print(i)
if __name__ == "__main__":
    main()