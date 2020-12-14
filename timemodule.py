import time

initial1 = time.time()
print(initial1)
for i in  range(45):
    print("hello")
    g = time.time() - initial1
print("for loop time = ",time.time()-initial1)  #for loop time =  0.001000046730041504


initial2 = time.time()
print("\n\n while loop start\n\n")

i = 0
while(i<45):
    print("hello")
    i +=1

print("while loop time = ", time.time() - initial2)  #while loop time =  0.001000046730041504
h = time.time() - initial2
print(g,"          ",h)



localtime = time.asctime(time.localtime(time.time()))

print(localtime)        #Thu Nov 19 23:11:50 2020


time.sleep(5)            #after 5  second it print sleep
print(" sleep")