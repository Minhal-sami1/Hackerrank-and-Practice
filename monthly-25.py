T = int(input())
for i in range(T):
    n = int(input())
    Prime = False
    # for checking s Prime
    if n % 2 != 0 or n == 2:
        if (n % 2) > 0:
            print("Not Prime")
        elif (n % 2) == 0:
            print("Prime")
