# exceptions are the key method of handling error in Python
# "try" something, then catch an "except"
# you can always raise your own exceptions with "raise"


def main():
    try:
        fh = open('xlines.txt')
    #   if typo isn't there, it'll run as normal
        for line in fh:
            print(line.strip())
    #     the strip method strips the string of any trailing new lines
    except IOError as e:
        # this as e encapsulated the error and directory in a variable
        print("Couldn't open the file,", e)
    #     except, by itself, will catch any error
    # if you further specify except with an IOError, it'll give you an error message when you have that particular error
    
    # else:



if __name__ == "__main__": main()
