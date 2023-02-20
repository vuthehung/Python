import numpy

def main():
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for i in range(n)], int)
    tmp = numpy.sum(arr, axis=0)
    mul = 1
    for i in range(len(tmp)):
        mul *= tmp[i]
    print(mul)
if __name__ == "__main__":
    main()