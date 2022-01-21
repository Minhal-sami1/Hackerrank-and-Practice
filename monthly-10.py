#!/bin/python3

import math
import os
import random
import re
import sys

def consective(n):
    conb = 0
    cont= 0
    total_count = 0
    for i in n:
        if (int(i) == 0 and total_count == 0):
            total_count = 1
            conb = cont
            cont = 0

        elif(int(i) == 1):
            cont += 1

        elif(int(i) == 0 and total_count != 0):
            if(cont > conb):
                conb = cont
                cont = 0
            else:
                cont = 0 
    print(conb)      


if __name__ == '__main__':
    n = int(input().strip())
    # Converting into Binary
    form = format(n, "b")
    test = f"{form}0"
    # Calculate and print consective number of 1's
    consective(test)