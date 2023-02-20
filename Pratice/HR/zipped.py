def main():
    n, x = map(int, input().split())
    l = []
    for _ in range(x):
        l.append(map(float, input().split()))
    for i in zip(*l):
        print(sum(i) / len(i))
if __name__ == "__main__":
    main()