# f = open("vinayak3.txt")
# print(f.readline())           #hello guys,
# print(f.readline())           #i am vinayak paimode
# print(f.readline())           #i am student
# print(f.readline())           #in new art commerse science college parner
# f.close()

# f = open("vinayak3.txt")
#
# print(f.tell())                # 0
# print(f.readline())           #hello guys,
# print(f.tell())                #13
# print(f.readline())            #i am vinayak paimode
# print(f.tell())                 #35
# print(f.readline())           #i am student
# print(f.tell())                #49
# print(f.readline())           #in new art commerse science college parner
# print(f.tell())                #91
# f.close()

f = open("vinayak3.txt","r+")
print(f.tell())                # 0
print(f.readline())            #hello guys,
print(f.tell())                #13
print(f.readline())            #i am vinayak paimode
f.seek(13)
print(f.tell())                 #13
print(f.readline())            #i am vinayak paimode
print(f.tell())                #35
print(f.readline())           #i am vinayak paimode
print(f.tell())                #49
f.close(