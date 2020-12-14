friends=["vinayak","shubham","gopal","sagar",5]
numbers=[10,30,20,50,40]
"""
print(friends)                   # output= ['vinayak', 'shubham', 'gopal', 'sagar', 5]
print(friends[2])                # output= gopal
print(friends[0:5])              # output= ['vinayak', 'shubham', 'gopal', 'sagar', 5]
print(friends[:])                # output= ['vinayak', 'shubham', 'gopal', 'sagar', 5]
print(friends[::1])              # output= ['vinayak', 'shubham', 'gopal', 'sagar', 5]
print(friends[::])               # output= ['vinayak', 'shubham', 'gopal', 'sagar', 5]
print(friends[2::2])             # output= ['gopal', 5]
"""
"""
#negative  slicing
print(friends[0:5:-1])          #output = []
print(friends[-1:5:1])          #output = [5]
print(friends[:-3:1])           #output = ['vinayak', 'shubham']
print(friends[-1:-5:1])         #output = []
print(friends[::-2])            #output = [5, 'gopal', 'vinayak']
print(friends[1:5:2])           #output = ['shubham', 'sagar']
print(friends[1:5:-2])          #output = []
print(friends[::-1])           #output = [5, 'sagar', 'gopal', 'shubham', 'vinayak']
"""

#functions
""" there are some function
1  sort()
2  reverse()
3  append()
4  insert()
5  remove()
6  pop()
7  clear()
8  copy()
9  count()
10 extend()
11 index()

"""

"""
print("before sort",numbers)        # output :-before sort [10, 30, 20, 50, 40]
numbers.sort()
print("after sort",numbers)        # output :-after sort [10, 20, 30, 40, 50]
print("before reverse",numbers)    # output :-before reverse [10, 20, 30, 40, 50]
numbers.reverse()
print("after reverse",numbers)     # output :-after reverse [50, 40, 30, 20, 10]

numbers.append(7)                 # output :-[50, 40, 30, 20, 10, 7]
print(numbers)

 # note :- if we take empty  list ie numbers[]  then we can apends number in number[]

number1 = []                        # there is declaration of list

number1.append(5)
number1.append(6)
number1.append(7)
print(number1)                       # output :-[5, 6, 7]
"""
"""
# insert
print("before inserting  ",numbers)            # output :-before inserting   [10, 30, 20, 50, 40]
numbers
print("after insering  ",numbers)              # output :-after removing  [10, 30, 50, 40]
"""
"""
#remove()
print("before removing  ",numbers)               #output :-before removing   [10, 30, 20, 50, 40]
numbers.remove(20)
print("after removing ",numbers)               #output :-after inserting   [10, 30, 50, 40]

#pop()
print("before pop  ",numbers)                 #output :-  before pop   [10, 30, 50, 40]
numbers.pop()
print("after pop  ",numbers)                  #output :-after pop   [10, 30, 50]
"""

"""
#tuple
#note:- if we have to dont change change the value in list the we use tuple
tuple1=(1,2,3,4)
print(tuple1)                                 #output:-(1, 2, 3, 4)
#tuple1[1]=10;                                 #output :- 'tuple' object does not support item assignment
tuple2=(1)
print(tuple2)                                  #output :- 1               IT IS NOT TUPLE
tuple3=(1,)
print(tuple3)                                  #output :- (1,)               IT IS NOT TUPLE
"""

#swaping
# in traditional technique we use   temp=a; a=b; b=temp;   but in python make it easy

a=10
b=20
print("before swaping a = ",a," b = ",b)   #output :- before swaping a =  10  b =  20
a,b=b,a
print("after swaping a = ",a," b = ",b)    # output :- after swaping a =  20  b =  10


num = numbers.index(20,0,6)                  #index 2
print("index",num)
# num = numbers.index(20,0,1)                   #ValueError: 20 is not in listj

