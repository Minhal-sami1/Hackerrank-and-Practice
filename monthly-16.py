#!/bin/python3
import sys



if __name__ == '__main__':
    S = input()
try:
    print(int(S))
except ValueError:
    print("Bad String")