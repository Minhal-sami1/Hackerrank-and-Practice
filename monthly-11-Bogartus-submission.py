#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
total = int(0)
maxTotal = int(-100)
    
#print (arr)
def hourglass(a,maxTotal):
    for i in range(1,5):
        for j in range(1,5):
#            print ('top left = ' + str(a[i-1][j-1]) + ' '+ str(i-1) + ',' + str(j-1))
#            print ('top mid = ' + str(a[i-1][j]) + ' '+ str(i-1) + ',' + str(j))
#            print ('top right = ' + str(a[i-1][j+1]) + ' '+ str(i-1) + ',' + str(j+1))
#            print ('mid mid = ' + str(a[i][j]) + ' '+ str(i) + ',' + str(j))
#            print ('bot left = ' + str(a[i-1][j+1]) + ' '+ str(i+1) + ',' + str(j-1))
#            print ('bot mid = ' + str(a[i][j+1]) + ' '+ str(i+1) + ',' + str(j))
#            print ('bot right = ' + str(a[i+1][j+1]) + ' '+ str(i+1) + ',' + str(j+1))
            total = a[i-1][j-1] + a[i-1][j] + a[i-1][j+1] + a[i][j] + a[i+1][j-1] + a[i+1][j] + a[i+1][j+1]
#            print (total)
            if total >= maxTotal:
                maxTotal = total

    print (maxTotal)

hourglass(arr,maxTotal)
#print (maxTotal)