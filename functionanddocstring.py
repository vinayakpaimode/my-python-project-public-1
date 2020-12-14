a = 9
b = 8
c = sum((a,b))             # built in function
print(c)

#user define function
def sum1(a,b):
    print("you are in function 1")
    print("sum is  ",a+b)   #  sum is   17

sum1(a,b)

def ave1(a,b) :
    average = (a + b)/2
    print(" in function average  = ",average)   #in function average  =  8.5
    return average
print("out of function",ave1(a,b))     #out of function 8.5
val = ave1(a,b)
print(val)                              #8.5

#docstring

def sum3(a,b) :
    """ this is a docstring you can print information about function """
    return a+b
1
print(sum3.__doc__)    #output =  this is a docstring you can print information about function

