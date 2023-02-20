import numpy

def main():
    arr = numpy.array(input().split(), float)
    print(numpy.floor(arr))
    print(numpy.ceil(arr))
    print(numpy.rint(arr))
if __name__ == "__main__":
    main()