
# author: zero
# usage: python rev_hash.py <hash_value>

import sys


def main(argv):
    try:
        arg = sys.argv[1]
    except:
        print "Error: No argument supplied. usage:$ python rev_hash.py <hash_value> "
        return
    # hash(sys.argv[1])
    rev_hash(sys.argv[1]) # take first argument as hash value to operate on

# from question
def hash(s):
    h = 7
    letters = "acdegilmnoprstuw"
    for i in range(len(s)):
        h = (h * 37 + letters.index(s[i]))
    print h

# required solution
def rev_hash(h):
    try:
        h = int(h)
    except ValueError:
        print("That's not an int!  example:$ python rev_hash.py 930846109532517 ")
        return

    # list to keep appending the letter (backward fashion),
    # finally we just reverse print the list to get string
    list = []
    letters = "acdegilmnoprstuw"
    while h is not 7:
        ix_ll = h % 37 # index of last letter
        h = (h - ix_ll)/37
        try:
            list.append(letters[ix_ll])
        except:
            print "invalid input hash_value"
            return
    string = ""
    for i in reversed(list):
        string+= i
    print string

if __name__ == "__main__":
    main(sys.argv[1:])
