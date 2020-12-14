def getdate():
    import datetime
    return datetime.datetime.now()
date = getdate()

print(type(date))
var6 = 30.8
print(" var6 =  ",type(var6))
while(1):
    print("which of student you enter \n 1 : vinayak \n 2: shubham \n 3: gopal  ")
    var1 = int(input())
    if (var1 > 3 or var1 < 1):
        print("invalid no you enter plz enter valid no bet 1 - 3")
        continue
    print("\n 1:exersize \n 2:diet")
    var2 = int(input())
    if (var2 > 2 or var2 < 1):
        print("invalid no you enter plz enter valid no bet 1-2")
        continue
    if (var1 == 1 and var2 == 1):  # vinayak exer
        print("what exersize you do")
        exer = input()
        fve = open("vinayakexer.txt", "a")
        fve.write("    ")
        fve.write("    ")
        fve.write(str(date))
        fve.write("    ")
        fve.write(exer)
        fve.write("\n")
        fve.close()

    elif (var1 == 1 and var2 == 2):  # vinayak diet
        print("what take in your diet")
        diet = input()
        fve = open("vinayakdiet.txt", "a")
        fve.write("    ")
        fve.write(str(date))
        fve.write("    ")
        fve.write(diet)
        fve.write("\n")
        fve.close()

    elif (var1 == 2 and var2 == 1):  # shubham exer
        print("what exersize you do")
        exer = input()
        fse = open("shubamexer.txt", "a")
        fse.write("    ")
        fse.write(str(date))
        fse.write("    ")
        fse.write(exer)
        fse.write("\n")
        fse.close()

    elif (var1 == 2 and var2 == 2):  # shubham diet
        print("what take in your diet")
        diet = input()
        fve = open("shubhamdiet.txt", "a")
        fve.write("    ")
        fve.write(str(date))
        fve.write("    ")
        fve.write(diet)
        fve.write("\n")
        fve.close()

    elif (var1 == 3 and var2 == 1):  # gopal exer
        print("what exersize you do")
        exer = input()
        fge = open("gopalexer.txt", "a")
        fge.write("    ")
        fge.write(str(date))
        fge.write("    ")
        fge.write(exer)
        fge.write("\n")
        fge.close()
    elif (var1 == 3 and var2 == 2):  # gopal diet
        print("what take in your diet")
        diet = input()
        fve = open("gopaldiet.txt", "a")
        fve.write("    ")
        fve.write(str(date))
        fve.write("    ")
        fve.write(diet)
        fve.write("\n")
        fve.close()
    print("if yo want to exit then enter y" )
    exit1 = input()
    if(exit1 == 'y'):
        exit()

# fse= open("subhamexer.txt","a")
# fse.write("hello")
# fse.close()
# fge = open("gopalexer.txt","a")
# fge.write("hello")
# fge.close()
# fvd = open("vinayakdiet.txt","a")
# fvd.write("hello")
# fvd.close()
# fsd= open("shubhamdiet.txt","a")
# fsd.write("hello")
# fsd.close()
# fgd = open("gopaldiet.txt","a")
# fgd.write("hello")
# fgd.close()