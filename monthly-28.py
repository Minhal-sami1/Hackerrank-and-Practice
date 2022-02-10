#!/bin/python3
import re

lst = []
if __name__ == '__main__':
    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if re.search('@gmail\.com$', emailID):
            lst.append(firstName)
    lst.sort()
    for i in lst:
        print(i)
