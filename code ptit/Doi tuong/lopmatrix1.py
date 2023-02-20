class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
    def mul_mtrix(self):
        for i in range(self.n):
            for j in range(self.n):
                x = 0
                for k in range(self.m):
                    x += (self.a[i][k] * self.a[j][k])
                print(x, end= ' ')
            print()

def solve():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = []
        for i in range(n):
            a.append([int(j) for j in input().split()])
        matrix = Matrix(n, m, a)
        matrix.mul_mtrix()
        

def main():
    solve()

if __name__ == "__main__":
    main()