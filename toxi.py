#!/usr/bin/env python3
import sys

def decode(filename):
    with open(filename) as f:
        read_data = f.read()

    letters = read_data.split(' ')
    ascii_letters = ([chr(int(x, 2)) for x in letters])

    phrase = ''
    for letter in ascii_letters:
        phrase += letter

    print(phrase)


if __name__=='__main__':
    filename = decode(sys.argv[1])
