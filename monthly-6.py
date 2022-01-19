num = int(input())
if(1 <= num and num <= 10):
    for i in range(0, num):
        string = input()
        leng = len(string) 
        if (leng >= 2 and leng <= 10000):
            for index in range(0, leng):
                if (index % 2 == 0):
                    print(string[index], end="")
            print(" ", end="")
            for sindex in range(0, leng):
                if(sindex % 2 != 0):
                    print(string[sindex], end="")
            print(" ")
