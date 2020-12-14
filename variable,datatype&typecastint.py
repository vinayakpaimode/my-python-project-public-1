var1 = "vinayak "
var2 = 3
var3 = 7.8
var4 = "paimode"
var5 = 50
var6 = "70"
var7 = "30"
counter = 1
print(type(var1))  # output=   <class 'str'>
print(type(var2))  # output=   <class 'int'>
print(type(var3))  # output=   <class 'float'>


#print(var1+var2)  # output=   its give an error
print(var1+var4)   # output=   vinayak paimode

print(var2+var3)   # output=   10.8

print(var6 + var7)            # output=   7030
# print(var6 + int(var5)) # output=    ValueError: invalid literal for int() with base 10: 'paimode'
    # note :- error was come therefor upper line is comment out

"""there are some type cast function:-
str() int()  float() """
print("paimode")     # output:- paimode
print(5 * "vinayak\n")
"""                         vinayak
                            vinayak
                            vinayak
                            vinayak
                            vinayak """

print(int(var6) + int(var7)) # output :- 100
print(5 * str(int(var6) + int(var7))) # output :-100100100100100


