import numpy

def main():
    n = int(input())
    a = numpy.array([input().split() for _ in range(n)], int)
    b = numpy.array([input().split() for _ in range(n)], int)
    print(numpy.dot(a, b))
if __name__ == '__main__':
    main()