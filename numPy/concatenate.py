
import numpy

def main():
    n, m, p = map(int, input().split())
    arr1 = numpy.array([input().split() for i in range(n)], int)
    arr2 = numpy.array([input().split() for i in range(m)], int)
    print(numpy.concatenate((arr1, arr2), axis=0))

if __name__ == "__main__":
    main()