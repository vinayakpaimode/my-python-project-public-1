while(1):
    a = int(input("enter no  of rows  "))
    b = int(input("enter only 0 and 1"))
    if (b > 1 or b < 0):
        print("please enter  only 0 and 1")
        continue
    c = bool(b)
    if c:
        for x in range(1, a + 1):
            for c in range(x):
                print("*", end=" ")
            print()
    else:
        for x in range(a, 0, -1):
            for c in range(x):
                print("*", end=" ")
            print()
    d = input("enter y if you want to exit")
    if (d == 'y'):
        exit()
