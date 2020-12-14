# f1 = open("vinayak1.txt","w")
# f1.write("vinayak paimode")
# f1.close()
#
# f2 = open("vinayak1.txt","a")
# noofchar =  f2.write("\nis a student")
# print("no of character =  ",noofchar)    #output :- no of character =   13
# f2.close()
# """output :-
# vinayak paimode
# is a student"""

""" handle read and write both
"""
f3 = open("vinayak1.txt","r+")
f3.write("shubham")
print(f3.read())
f3.write("thanks")
f3.close()
