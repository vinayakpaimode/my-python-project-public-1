#global scope
l = 10
# def function1(n):
#     l = 5  #local
#     m = 40
#     print("in  l =>  ",l)
#     print(n,"i have printed ")
#
# function1("this is vinayak ")
# print("out = ",l)

# def function1(n):

# l = l + 20           #if we write here directly the it give error
# UnboundLocalError: localn variable 'l' referenced before assignment
#     global l
#     l = l + 90
#     print("in  l =>  ",l)     #in  l =>   100
#     print(n,"i have printed ") #this is vinayak  i have printed
#
# function1("this is vinayak ")
# print("out = ",l)          #out =  100
#
x =  89
def vinayak1():
    x = 40
    def paimode():
        global x
        x = 80
    print("before calling paimode()",x) #before calling paimode() 40
    paimode()
    print("after calling paimode()",x) #after calling paimode() 40

vinayak1()

print(x)   #80  # ethe x ha global variabe automatic banvle aahe