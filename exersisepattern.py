print("enter no of rows ")
var1 = int(input())
print("enter 0 or 1 ")
var3 = int(input())

var5 = var1
var4 = bool(var3)
var6 = 0
var7 = 0
var2 = 0
while(var6<var1) :
    while(var7<var1):
        if(var4==True):
            if(var3 >= var5):
                print("*",end=" ")
        else:
            if (var3 <= var5):
                print("*", end=" ")
        var7 +=1
    print()
    var6 +=1
