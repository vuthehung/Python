import numpy

def main():
    a = numpy.array(input().split(), int)
    b = numpy.array(input().split(), int)
    print(numpy.inner(a, b))
    print(numpy.outer(a, b))
if __name__ == '__main__':
    main()