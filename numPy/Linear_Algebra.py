import numpy


def main():
    n = int(input())
    arr = numpy.array([input().split() for _ in range(n)], float)
    print(numpy.around(numpy.linalg.det(arr), 2))

if __name__ == "__main__":
    main()