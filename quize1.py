print("enter your age ",end=" ")
age = int(input())

if age>5 and age<101 :
    if age > 18 :
        print("you can drive")
    else :
        print("you cant drive")
    if age == 18:
        print("invalid")
else :
    print("nochance")


"""output :-
enter your age  19
 you can drive
"""
