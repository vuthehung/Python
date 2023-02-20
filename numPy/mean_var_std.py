#var: variance: phuong sai
#std: standard: do lech chuan

import numpy

def main():
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for i in range(n)], int)
    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    print(numpy.around(numpy.std(arr), 11))

if __name__ == "__main__":
    main()