#range
# for i in range(5):
#     print(i,end = " ")     #0 1 2 3 4

# a = range(1,5)
# for d in a :
#     print(d,end=" ")          #1 2 3 4
# print()
# a = range(1,10,2)
# for d in a :
#
#     print(d,end=" ")          #1 3 5 7 9
#
# print()
# a = range(10,0,-1)
# for d in a :
#
#     print(d,end=" ")          #10 9 8 7 6 5 4 3 2 1 0
#
# print()
# a = range(-10,0,1)
# for d in a :
#
#     print(d,end=" ")          #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1


st = "vinayak"
n= len(st)
for i in range(n):
    print(i,"=",st[i])
#output :=
# 0 = v
# 1 = i
# 2 = n
# 3 = a
# 4 = y
# 5 = a
# 6 = k


"""                        for loop with else             """

st = "vinayak paimode"
n= len(st)
for i in range(n):
    print(i,"=",st[i])
else:
    print("else part")

"""# 0 = v
# 1 = i
# 2 = n
# 3 = a
# 4 = y
# 5 = a
# 6 = k
# 7 =
# 8 = p
# 9 = a
# 10 = i
# 11 = m
# 12 = o
# 13 = d
# 14 = e
# else part
"""