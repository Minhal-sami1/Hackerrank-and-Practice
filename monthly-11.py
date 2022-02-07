#!/bin/python3
def calculate(arr):
    every_sum = []
    # address every hour glass
    for i in range(6):
        for j in range(6):
            rows = [i-1, i, i+1]
            cols = [j-1, j, j+1]
            # Check if the index of 3x3 array is not negative and not greater than 6
            check_cols = all(t >= 0 and t <= 5 for t in cols)
            check_rows = all(o >= 0 and o <= 5 for o in rows)
            number_of_arrays = 0
            sum_of_cols = 0
            for k in range(3):
                # Check if any 3x3 array we are getting is greater than 0 and less than 6
                if (check_cols and check_rows):
                    number_of_arrays += 1
                    for l in range(3):
                        # Access the hourglass: arr[rows[k]][cols[l]]

                        # Sum Them Up
                        if(k == 1):
                            sum_of_cols += int(arr[rows[k]][cols[1]])
                            break

                        elif(k != 1):
                            sum_of_cols += int(arr[rows[k]][cols[l]])

            if(number_of_arrays > 0):
                every_sum.append(sum_of_cols)
                sum_of_cols = 0
    print(max(every_sum))


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    calculate(arr)
