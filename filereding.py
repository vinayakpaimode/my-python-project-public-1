
f1 = open("vinayak.txt","rt")   # rt was optional and default if we read file in binary mode then use rb
content1 = f1.read()
print(content1)
"""" output :-
 Hello i am vinayak
 my best friends are :
 gopal shubham sagar
 """
f1.close()
f2 = open("vinayak.txt","rt")
content2 = f2.read(3)
print(content2)        # output ->Hel

f2.close()

f3 = open("vinayak.txt","rt")
content3 = f3.read(3)
print(content3)                     #output ->Hel
content3 = f3.read(3)
print(content3)                      #output ->lo
f3.close()


f4 = open("vinayak.txt","rdfwdt")
content4 = f4.read()
counter = 0
for line in content4 :
    print(line,end="")      #output -> Hello i am
    counter += 1
    if (counter == 10) :
        break
f4.close()

44` f5 = open("vinayak.txt","rt")        # it say print data line by line
for line in f5 :
    print("\n",line,end="")       #output ->Hello i am vinayak
    break
f5.close

         #readline
f6 = open("vinayak.txt","rt")
print(f6.readline())   #output ->Hello i am vinayak
print(f6.readline())   #output ->my best friends are :
print(f6.readline())   #output ->gopal shubham sagar
f6.close

         #readlines it create a list
f7 = open("vinayak.txt","rt")   #output->['Hello i am vinayak\n', 'my best friends are :\n', 'gopal shubham sagar']
print(f7.readlines())
f7.close


""" total output :-
Hello i am vinayak
my best friends are :
gopal shubham sagar
Hel
Hel
lo
Hello i am
 Hello i am vinayak
Hello i am vinayak

my best friends are :

gopal shubham sagar
['Hello i am vinayak\n', 'my best friends are :\n', 'gopal shubham sagar']

"""