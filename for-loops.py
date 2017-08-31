def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        # readlines is an iterator that takes one object at a time
        # and returns in one at at time, in this case into the line variable
        print(line, end='')
#       print function prints a blank line after each line

if __name__ == "__main__": main()

# all container types, lists, variables, strings, ranges, etc; are iterables
# you can iterate/loop through them

# for loop syntax:
# for variable in container:
#   print(variable)