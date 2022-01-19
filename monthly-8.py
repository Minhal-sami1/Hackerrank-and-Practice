from ast import Try


n = int(input())
phone_book = dict(input().split() for x in range(n))
while True:
    try:
        name = input()
        if (phone_book.get(name) != None):
            print(name + '=' + phone_book[name])
        else:
            print("Not found")
    except EOFError:
        break;  
 
