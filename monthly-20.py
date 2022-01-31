#!/bin/python3
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    sum_of_swaps = []
    # Write your code here
    for i in range(0, n):
        # Tracking swaps everytime new iteration; it is to check if no swap takes places so break
        number_of_swaps = 0
        for j in range(0, n-1):
            if (a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                number_of_swaps += 1
        
        if( number_of_swaps == 0 ):
            break
        else:
            sum_of_swaps.append(number_of_swaps)
        
    print("Array is sorted in {} swaps.".format(sum(sum_of_swaps)))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[n-1]))