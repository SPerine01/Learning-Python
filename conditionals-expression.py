def main():
    a, b = 0, 1
    v = 'this is true' if a < b else 'this isn\'t true'
    # if a < b:
    #     v = 'this is true'
    # else:
    #     v = 'this isn\'t true'
    # v is placed in an expression and it condenses the code
    # the if/else makes it a conditional expression
    print(v)

if __name__ == "__main__": main()