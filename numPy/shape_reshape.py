#chuyen doi tu mang thanh ma tran



import numpy

def main():
    a = input().split(' ')
    arr = numpy.array(a, int)
    print(numpy.reshape(arr, (3, 3)))
if __name__ == "__main__":
    main()