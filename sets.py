s = set()
print(type(s))    # output -:-<class 'set'>
sfromlist = set([1,2,3,4])
print(sfromlist)     #output;-{1, 2, 3, 4}
#functions
# 1 add
s.add(1)
s.add(1)           #it never takes double value it is unique
s.add(2)
print(s)                     #output:-   {1, 2}

s1 = s.union([1,2,3,4])
print(s,s1)                   #output;-{1, 2} {1, 2, 3, 4}

s2 = s.intersection([1,2,3,4])
print(s,s2)                      #output:-{1, 2} {1, 2}

#len()

print("length of set  ",len(s))       #output = length of set   2
#min()
print("minimum value of set  ",min(s))       #output = minimum value of set   1
#max()
print("maximum value of set  ",max(s))       #output = maximum value of set   2

# disjoint()
print(s.isdisjoint(s1))                       #output = False

#remove()
print("before removing s ",s)  #output=before removing s  {1, 2}
s.remove(2)
print("after removing s ",s)   #output=after removing s  {1}

