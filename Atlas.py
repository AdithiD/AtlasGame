import random
f1 = open("atlas.txt","r", encoding="utf-8", errors="ignore")
words=[i.replace('\n' ,'') for i in f1.readlines()]
lastchar1 = ""
lastchar2 = ""
userchoice = input("user : ").lower()
if userchoice in words:
    words.remove(userchoice)
    lastchar1 = userchoice[-1]
    temp = list(filter(lambda x:x.startswith(lastchar1),words))
    randnum = random.randrange(0,len(temp))
    computerchoice = temp[randnum]
    print("Computer :",computerchoice)
    words.remove(computerchoice)
    lastchar2 = computerchoice[-1]
    for i in range(0,47868,1):
        userchoice = input("user : ")
        if userchoice.startswith(lastchar2) and (userchoice in words):
            lastchar1 = userchoice[-1]
            temp = list(filter(lambda x:x.startswith(lastchar1),words))
            randnum = random.randrange(0,len(temp))
            computerchoice = temp[randnum]
            print("Computer :",computerchoice)
            words.remove(computerchoice)
            lastchar2 = computerchoice[-1]
        else:
            print("Computer wins")    
            break
else:
    print("Invalid Input !!!")
