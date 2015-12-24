myL = [1,1,1,3,1,2,2,1,1,3]
count = 1
myNewL = []
curDig = myL[0]
#myNewL.append(curDig)
howMany = 0

while(howMany < 50):
    for i in range(1, len(myL)):
        if myL[i] == curDig:
            count = count + 1
            if (i == len(myL) - 1):
                myNewL.append(count)
                myNewL.append(curDig)
        else:
            myNewL.append(count)
            myNewL.append(curDig)
            count = 1
            curDig = myL[i]
            if (i == len(myL) - 1):
                myNewL.append(count)
                myNewL.append(curDig)
    #print myL
    myL = myNewL
    myNewL = []
    curDig = myL[0]
    count = 1
    howMany = howMany + 1

print len(myL)

#40wrong: 258598
#40right: 360154

#50right: 5103798
