"""
types of operater
1 arithmatics
2 comparison
3 logical operater
4 identity operater
5 membership operater
6 bitwie operater
"""
#arithmatic operater
print("5+6  = ",5+6)                    #output:-   5+6  =  11
print("5-6  = ",5-6)                    #output:-   5-6  =  -
print("5*6  = ",5*6)                    #output:-   5*6  =  30
print("5/6  = ",5/6)                    #output:-   5/6  =  0.8333333333333334
print("5//6  = ",5//6)                  #output:-   5//6  =  0
print("15//6  = ",15+6)                 #output:-   15//6  =  21
print("5**6  = ",5**6)                  #output:-   5**6  =  15625

#assignment operater
x = 5
print(x)
x+=7                                 # all type of arith matics oprater
print(x)

#comparison operater
print(5<=6)                            #output :-True

#logical operater
a=True
b=False
print(a and b)               #output = False
print(a or b)                #output = True

#identity operater
print(a is b)                 #output =False
print(a is not b)              #output =True

#membership operater
list = [1,2,3,4,5,6,7,8,9 ]
print(4 in list)               #output =True
print(10 in list)              #output =False
print(10 not in list)              #output =True
print(4 not in list)              #output =False

#bitwise operater
print(0 & 1)               #output =0
print(0 | 1)               #output =1

print(4 | 1)               #output =5