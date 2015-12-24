rf = open('advent8.txt', 'r')
i = len(rf.readlines())
rf.seek(0)
totalcode = 0
totalmem = 0

for i in range(0, i):
        totalmem = totalmem - 2
        line = list(rf.readline().strip("\n"))
       # print eval(str(line))
       # print str(line)
        totalcode = totalcode + len(line)
        for x in range(0, len(line) - 1):
		
                if line[x] == "\\" and switch == False:
                        if line[x+1] == "\"":
                                totalmem = totalmem - 1
                        elif line[x+1] == "\\":
                                totalmem = totalmem - 1
                                switch = True
                                #print line[x], line[x+1]
                        elif line[x+1] == "x":
                                if ord(line[x+2]) < ord('g') and ord(line[x+3]) < ord('g'):
                                        totalmem = totalmem - 3
                                       # print line[x+2], line[x+3]
                else:
                        switch = False
                
                
                                
print totalcode
totalmem = totalmem + totalcode
print totalcode - totalmem
 
#total code = 6310, 4959
# \"
# \\
# \x ##
# \\ \x5c -> \\ -> \
