l1 = [1,2,3,4,5,6]
i = 1
a = 2
for i in l1:
    if i % 2 is not 0:
        print(i)
    i +=1

for index, item in enumerate(l1):
    if index%2==0:
        print(item)

