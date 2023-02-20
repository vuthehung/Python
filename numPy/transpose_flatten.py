import numpy

def main():
    n, m = input().split()
    arr = numpy.array([input().split() for i in range(int(n))], int)
    print(arr.transpose())
    print(arr.flatten())
if __name__ == "__main__":
    main()