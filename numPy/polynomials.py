import numpy

def main():
    arr = numpy.array(input().split(), float)
    x = float(input())
    print(numpy.polyval(arr, x))
if __name__ == "__main__":
    main()