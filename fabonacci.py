num = int(input("enter number"))

def fabonacci(num1):
    fabo = 1
    if num1==1:
        return 1
    elif num1 == 2:
        return 1
    else :
        fabo = fabonacci(num1 - 1) + fabonacci(num1 - 2)

        return fabo

#print("the num of nth position ",fabonacci(num))

for i in range(num) :
   no = fabonacci(i + 1)
   print(no)
