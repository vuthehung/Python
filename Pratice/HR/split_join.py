def split_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
if __name__ == '__main__':
    s = input()
    res = split_join(s)
    print(res)