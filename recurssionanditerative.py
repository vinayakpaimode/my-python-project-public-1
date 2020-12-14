# def print2(str2):
#     print("this is ",str2)  #this is  vinayak
# print2("vinayak")
while(1):

    def factite(n):
        fac = 1
        for i in range(n):
            fac = fac * (i + 1)
        return fac


    def factfun(n):
        fac = 1
        if (n == 1):
            return 1
        else:
            fac = n * factfun(n - 1)
            return (fac)


    n = int(input("enter no"))

    print("factorial factfun() => ", factfun(n))  # output ->factorial factfun() =>  120
    print("factorial factite()=> ", factite(n))  # output ->factorial factite()=>  120
    print("----------------------------------------------------------------------------")
    print("enter  y when exit ")
    exit1 = input()
    if(exit1=='y'):
        exit()

    print("----------------------------------------------------------------------------")


