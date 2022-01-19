#!/bin/python3

import math
import os
import random
import re
import sys
from unittest import result



if __name__ == '__main__':
    n = int(input().strip())
    res = ["{} x {} = {}".format(n, i, n*i) for i in range(1, 11)]
    for i in res:
        print(i)