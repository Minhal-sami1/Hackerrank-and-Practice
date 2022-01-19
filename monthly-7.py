#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    leng = len(arr)
    result = [arr[i] for i in range(leng-1, -1, -1)]
    print(*result, end=" ")
