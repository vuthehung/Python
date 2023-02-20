import numpy

def main():
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for i in range(n)], int)
    tmp = numpy.min(arr, axis=1)
    print(numpy.max(tmp))
if __name__ == "__main__":
    main()