
# author: zero
# usage: python rev_hash.py <hash_value>

import sys


def main(argv):
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
    h = int(h)
    # list to keep appending the letter (backward fashion),
    # finally we just reverse print the list to get string
    list = []
    letters = "acdegilmnoprstuw"
    while h is not 7:
        ix_ll = h % 37 # index of last letter
        h = (h - ix_ll)/37
        list.append(letters[ix_ll])
    string = ""
    for i in reversed(list):
        string+= i
    print string

if __name__ == "__main__":
    main(sys.argv[1:])
