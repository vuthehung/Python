import numpy

def main():
    n, m = map(int, input().split())
    a = numpy.array([input().split() for i in range(n)], int)
    b = numpy.array([input().split() for i in range(n)], int)
    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print(numpy.divide(a, b))
    print(numpy.mod(a, b))
    print(numpy.power(a, b))
if __name__ == "__main__":
    main()