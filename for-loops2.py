def main():
    fh = open('lines.txt')
    for index,line in enumerate(fh.readlines()):
        print(index, line, end='')
#the enumerate functions adds numbers to the value you're iterating
#it takes 2 values, the index and the value from the iterator
# the index starts at 0, unless you state underwise


if __name__ == "__main__": main()


s = 'this is a string'
for i, c in enumerate(s, start=1):
    # remember, i is the index, c is the value of the iterator
    if c == 's':
        print('index {} is an s'.format(i))

