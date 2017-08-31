# reading and writing text files

#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com

def main():
    # how to write to a text file
    # infile = open('lines.txt', 'r')
    # outfile = open('new.txt', 'w')
    # for line in infile:
    #     print(line, file= outfile, end = '')
    # print('Done')


    buffersize = 5000
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt', 'w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        buffer = infile.read(buffersize)
        print('.', end = '')
        print()
    print('Done')

if __name__ == "__main__": main()
