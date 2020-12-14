count = 1
i=1
while(i<10):
    print("-------------------------------------------------------")
    print("you have ",10 - count, "gesses are limt")

    no = int(input("enter number "))
    if(no==18):
        print(" you enter right number")
        print("you required only ",count," guesses")
        break
    elif(no < 18) :
        print("enter biger no")
    elif(no > 18):
        print(" enter smaller no")
    i+=1
    count=count+1
    
print("--------------------sorry game over------------------------")

