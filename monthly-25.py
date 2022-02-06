from math import sqrt

T = int(input())
for i in range(T):
    n = round(int(input()))
    div = round(sqrt(n))+1
    if n == 1:
        print("Not prime")
        continue
    elif n % 2 != 0:
        for j in range(2, div):
            if n % j == 0:
                print("Not prime")
                break
        else:
            print("Prime")
    elif n == 2:
        print("Prime")
    elif n % 2 == 0:
        print("Not prime")
