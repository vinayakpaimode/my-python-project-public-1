list1 = [["gopal",1],["sagar",2],["shubham",3],["vinayak",4]]
#list1 = ["gopal","sagar","shubham","vinayak"]
counter1 = 0
counter3 = 0
for item1,num1 in list1 :
    print(counter3,"item is =  ",end=" ")
    counter3 = counter3+1
    print(item1," num ",num1)
""" output :-
0 item is =   gopal  num  1
1 item is =   sagar  num  2
2 item is =   shubham  num  3
3 item is =   vinayak  num  4
"""
#p
for item2 in list1 :
    print(counter1,"item is =  ",end=" ")
    counter1 = counter1+1
    print(item2)

"""output :-
0 item is =   ['gopal', 1]
1 item is =   ['sagar', 2]
2 item is =   ['shubham', 3]
3 item is =   ['vinayak', 4]
"""

# list to dict conversion

list2 = [["gopal",1],["sagar",2],["shubham",3],["vinayak",4]]

dict1 = dict(list2)
print(dict1)           #output:- {'gopal': 1, 'sagar': 2, 'shubham': 3, 'vinayak': 4}

print(dict1.items())    #output:- dict_items([('gopal', 1), ('sagar', 2), ('shubham', 3), ('vinayak', 4)])

counter2 =0
for item2,num1 in dict1.items() :
    print(counter2,"item is =  ",item2," number is  ",num1)
    counter2 = counter2+1
"""output :-
0 item is =   gopal  number is   1
1 item is =   sagar  number is   2
2 item is =   shubham  number is   3
3 item is =   vinayak  number is   4
"""
