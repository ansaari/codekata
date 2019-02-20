print("welcome to stack")
ser=["insert a value fom the list","remove value from the list","find the length of the list","check it is empty or not","exit"]
pos=["front","rear"]
exit=["yes","no"]
a=[]
while True:
    print("which one of our service did you want?\n1.insert a value fom the list \n2.remove value from the list \n3.find the length of the list\n4.check is is empty or not \n5.exit")
    customerchoice=int(input())
    if customerchoice==1:
        print("you are select to",ser[customerchoice-1])
        print("please enter the value")
        invalue=input()
        print("where do you want to enter the value?\n1.front\n2.rear")
        posinvalue=int(input())
        print("you are select to insert in",pos[posinvalue-1],"side")
        
        if posinvalue==1:
             a.insert(0,invalue)
             print("now your list is",a) 
        else:
              a.append(invalue) 
        print("now your list is:",a)
    elif customerchoice==2:
        print("you are select to",ser[customerchoice-1])  
        if len(a)==0:
            print("it is a empty list")
        else:
            print("where do you want to remove the value?\n1.front\n2.rear")
            posremvalue=int(input())
            print("you are select to remove in",pos[posremvalue-1],"side")
            if posremvalue==1:
                a.pop(0)
            else:
                a.pop()
            print("now your list is",a)
    elif customerchoice==3:
        print("you are select to",ser[customerchoice-1])  
        print("now your list has",len(a),"values")
    elif customerchoice==4:
        print("you are select to",ser[customerchoice-1])  
        if len(a)==0:
            print("your list is empty")
        else:
            print("your list is not empty and your list is:",a)
    else:
        print("are you confirm to",ser[customerchoice-1])
        print("thank you,visit again")
        break
