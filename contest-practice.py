#code
t = int(input())
for i in range(0, t):
    password = input()
    tests = False
    test_upper = False
    test_lower = False
    test_number = False
    for i in password:
        if (i.isupper() == True):
            test_upper = True
        if (i.islower() == True):
            test_lower = True
        test_number = i.isnumeric()
  
    if(test_upper == True and test_lower == True and test_number == True):
        tests = True
        if (tests == True ):
            print("YES")
    else:
        print("NO")