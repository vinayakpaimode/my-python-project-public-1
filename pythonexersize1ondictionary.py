#crete a dictionary and take input from the user and return the meaning of the word from dictoionary

dict = {"vinu":"80","shubhu":"90","ram":"75"}
print("enter key as a string")
key1 = input()
print("enter item")
item1 = input()

print("enter key as a string")
key2 = input()
print("enter item")
item2 = input()

print("enter key as a string")
key3 = input()
print("enter item")
item3 = input()

print("enter key as a string")
key4 = input()
print("enter item")
item4 = input()

dict.update({key1:item1,key2:item2,key3:item3,key4:item4})
print(dict)
print("enter the key that you want to search  ",end=" ")
search1 = input()
search2=dict.get(search1)
print(search2)


"""enter key as a string
q
enter item
wq
enter key as a string
w
enter item
w
enter key as a string
e
enter item
e
enter key as a string
r
enter item
r
{'vinu': '80', 'shubhu': '90', 'ram': '75', 'q': 'wq', 'w': 'w', 'e': 'e', 'r': 'r'}
enter the key that you want to search   vinu
80
"""